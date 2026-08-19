"""
=============================================================
  GEO Explorer — MCP Service
  handlers.py — Lógica dos endpoints
=============================================================
"""
import json, os, random
from datetime import datetime
from config import PAISES_JSON, CERTS_DIR

# ── Caminho do novo JSON de tecnologias ───────────────────
BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
TECH_JSON = os.path.join(BASE_DIR, "..", "DATA", "tecnologias.geo_json")


# ══════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════

def _carregar_paises():
    with open(PAISES_JSON, encoding="utf-8-sig") as f:
        return json.load(f)["paises"]

def _buscar_pais(nome):
    for p in _carregar_paises():
        if nome.lower() in p["nome"].lower():
            return p
    return None

def _carregar_tecnologias():
    with open(TECH_JSON, encoding="utf-8-sig") as f:
        return json.load(f)["tecnologias"]

def _buscar_tecnologia(nome: str):
    """Busca parcial e case-insensitive no nome e categoria."""
    n = nome.lower()
    for t in _carregar_tecnologias():
        if n in t["nome"].lower() or n in t["categoria"].lower():
            return t
    return None


# ══════════════════════════════════════════════════════════
#  HANDLER: /geo — dados de um país
# ══════════════════════════════════════════════════════════

def handle_geo(pais_nome: str) -> dict:
    if not pais_nome:
        return {"status": 400, "erro": "Parâmetro 'pais' obrigatório"}
    pais = _buscar_pais(pais_nome)
    if not pais:
        return {"status": 404, "erro": f"País '{pais_nome}' não encontrado",
                "sugestoes": [p["nome"] for p in _carregar_paises()]}
    return {"status": 200, "pais": pais}


# ══════════════════════════════════════════════════════════
#  HANDLER: /trilha_geo — plano de estudo
# ══════════════════════════════════════════════════════════

def handle_trilha_geo(tecnologia: str) -> dict:
    """Retorna plano de estudo completo baseado na tecnologia."""
    if not tecnologia:
        return {"status": 400, "erro": "Parâmetro 'tecnologia' é obrigatório"}

    tech = _buscar_tecnologia(tecnologia)
    if not tech:
        todas = [{"id": t["id"], "nome": t["nome"], "categoria": t["categoria"],
                  "nivel": t["nivel"]} for t in _carregar_tecnologias()]
        return {"status": 404,
                "erro": f"Tecnologia '{tecnologia}' não encontrada",
                "sugestoes": todas}

    # Gera cronograma distribuindo módulos por semana (2 por semana)
    cronograma, semana = [], 1
    for i, mod in enumerate(tech["modulos"]):
        if i > 0 and i % 2 == 0:
            semana += 1
        cronograma.append({
            "semana":  semana,
            "modulo":  mod["id"],
            "titulo":  mod["titulo"],
            "tipo":    mod["tipo"],
            "carga":   mod["carga"],
            "xp":      mod["xp"],
        })

    # Agrupa módulos por fase
    teorias   = [m for m in tech["modulos"] if m["tipo"] == "teoria"]
    praticas  = [m for m in tech["modulos"] if m["tipo"] == "pratica"]
    projetos  = [m for m in tech["modulos"] if m["tipo"] == "projeto"]

    return {
        "status": 200,
        "trilha": {
            "id":                  tech["id"],
            "nome":                tech["nome"],
            "categoria":           tech["categoria"],
            "nivel":               tech["nivel"],
            "modulos":             tech["numero_de_modulos"],
            "xp_total":            tech["xp_total"],
            "carga_horaria":       tech["carga_horaria_total"],
            "badges":              tech["badges"],
            "lives":               tech["lives"],
            "pre_requisitos":      tech["pre_requisitos"],
            "tecnologias_usadas":  tech["tecnologias_usadas"],
            "promocao_vitalicia":  tech["promocao_vitalicia"],
            "certificado":         tech["certificado_disponivel"],
        },
        "cronograma":        cronograma,
        "total_semanas":     semana,
        "fases": {
            "teoria":  len(teorias),
            "pratica": len(praticas),
            "projeto": len(projetos),
        },
    }


# ══════════════════════════════════════════════════════════
#  HANDLER: /desafio_geo — gera desafio de código
# ══════════════════════════════════════════════════════════

_NIVEIS = {
    "iniciante":     ("Iniciante",     200, "15min"),
    "intermediario": ("Intermediário", 500, "45min"),
    "intermediário": ("Intermediário", 500, "45min"),
    "avancado":      ("Avançado",     1000, "90min"),
    "avançado":      ("Avançado",     1000, "90min"),
}

_ENUNCIADOS = {
    "Iniciante": [
        "Crie um mapa simples exibindo os países fronteiriços do Brasil.",
        "Carregue um arquivo GeoJSON e exiba seus atributos em tabela.",
        "Calcule a distância em km entre duas capitais usando coordenadas.",
        "Plote pontos de capitais de um continente em um mapa base.",
    ],
    "Intermediário": [
        "Implemente uma análise de buffer de 50km em torno de uma cidade.",
        "Crie uma consulta SQL espacial que retorna todos os países a menos de 500km.",
        "Desenvolva um script que classifica países por área em quartis e colore o mapa.",
        "Construa uma API REST que retorna dados geográficos filtrados por continente.",
    ],
    "Avançado": [
        "Implemente o algoritmo de Dijkstra adaptado para roteamento geoespacial.",
        "Crie um pipeline de ML para classificar uso do solo com imagens Sentinel-2.",
        "Desenvolva um dashboard em tempo real de dados climáticos com WebSocket.",
        "Implemente um índice espacial R-Tree para busca de pontos mais próximos.",
    ],
}

def handle_desafio_geo(tecnologia: str, nivel: str = "Intermediário") -> dict:
    """Gera um desafio de código geoespacial aleatório."""
    if not tecnologia:
        return {"status": 400, "erro": "Parâmetro 'tecnologia' é obrigatório"}

    nivel_info = _NIVEIS.get(nivel.lower().replace("á","a").replace("é","e"),
                              ("Intermediário", 500, "45min"))
    nivel_norm, xp, tempo = nivel_info

    tech = _buscar_tecnologia(tecnologia)
    badge = tech["badges"][0] if tech else f"{tecnologia} Explorer"
    categoria = tech["categoria"] if tech else "Geotecnologia"

    banco = _ENUNCIADOS.get(nivel_norm, _ENUNCIADOS["Intermediário"])
    enunciado = random.choice(banco)

    return {
        "status": 200,
        "desafio": {
            "tecnologia":  tecnologia,
            "categoria":   categoria,
            "nivel":       nivel_norm,
            "titulo":      f"Desafio GEO — {tecnologia} | {nivel_norm}",
            "enunciado":   enunciado,
            "xp":          xp,
            "tempo":       tempo,
            "badge":       badge,
            "dicas": [
                "Leia o enunciado com atenção antes de iniciar.",
                "Comece pelo caso mais simples (happy path).",
                "Documente cada etapa do processo.",
            ],
            "criterios": {
                "corretude": "40%",
                "qualidade_cartografica": "20%",
                "eficiencia": "20%",
                "documentacao": "20%",
            },
        },
    }


# ══════════════════════════════════════════════════════════
#  HANDLER: /certificado_geo — gera e salva certificado
# ══════════════════════════════════════════════════════════

def handle_certificado_geo(nome: str, tecnologia: str) -> dict:
    """Gera e salva certificado fictício em Markdown."""
    if not nome or not tecnologia:
        return {"status": 400, "erro": "Parâmetros 'nome' e 'tecnologia' são obrigatórios"}

    tech     = _buscar_tecnologia(tecnologia)
    xp       = tech["xp_total"]       if tech else 500
    nivel    = tech["nivel"]           if tech else "Intermediário"
    badges   = tech["badges"]          if tech else [f"{tecnologia} Explorer"]
    lives    = tech["lives"]           if tech else []
    carga    = tech["carga_horaria_total"] if tech else "N/A"
    nome_tec = tech["nome"]            if tech else tecnologia
    categoria= tech["categoria"]       if tech else "Geotecnologia"
    modulos  = tech["numero_de_modulos"] if tech else 0

    cert_id  = f"GEO-2026-{abs(hash(nome + tecnologia)) % 99999999:08d}"
    data_hj  = datetime.now().strftime("%d/%m/%Y")
    slug     = nome.lower().replace(" ", "-")
    data_slug= datetime.now().strftime("%Y%m%d")

    conteudo = f"""# 🌍 CERTIFICADO DE CONCLUSÃO — GEO Explorer

```
 ██████╗ ███████╗ ██████╗
██╔════╝ ██╔════╝██╔═══██╗
██║  ███╗█████╗  ██║   ██║
██║   ██║██╔══╝  ██║   ██║
╚██████╔╝███████╗╚██████╔╝
 ╚═════╝ ╚══════╝ ╚═════╝
       GEO Explorer
```

---

## ✨ {nome.upper()} ✨

**concluiu com êxito a trilha:**

## 🌐 {nome_tec}

| Campo | Detalhes |
|-------|----------|
| 📂 Categoria | {categoria} |
| 📊 Nível | {nivel} |
| 📦 Módulos | {modulos}/{modulos} ✅ |
| ⭐ XP | {xp} XP |
| 🕐 Carga Horária | {carga} |
| 🏅 Badges | {' • '.join(badges)} |
| 📅 Conclusão | {data_hj} |
| 🆔 ID | {cert_id} |

### 🏆 Badges
{"".join(f"🏅 **{b}**  " for b in badges)}

### 📺 Lives Assistidas
{"".join(f"  ✅ {l}\\n" for l in lives)}

---

> 🔒 https://geoexplorer.app/certificate/{cert_id}
> 🌍 GEO Explorer — _Explore o Mundo pelos Dados_

_Certificado Fictício — GEO Explorer v1.0.0_
"""

    os.makedirs(CERTS_DIR, exist_ok=True)
    filepath = os.path.join(CERTS_DIR, f"cert-{slug}-{data_slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(conteudo)

    return {
        "status": 201,
        "certificado": {
            "id":        cert_id,
            "usuario":   nome,
            "tecnologia": nome_tec,
            "categoria": categoria,
            "nivel":     nivel,
            "xp":        xp,
            "carga":     carga,
            "badges":    badges,
            "data":      data_hj,
            "arquivo":   filepath,
            "verificacao": f"https://geoexplorer.app/certificate/{cert_id}",
        },
    }


# ══════════════════════════════════════════════════════════
#  HANDLER: lista países
# ══════════════════════════════════════════════════════════

def handle_lista_paises() -> dict:
    paises = _carregar_paises()
    return {"status": 200, "total": len(paises),
            "paises": [{"id": p["id"], "nome": p["nome"], "capital": p["capital"],
                        "continente": p["continente"], "nivel": p["nivel"],
                        "xp": p["xp"]} for p in paises]}


# ══════════════════════════════════════════════════════════
#  HANDLER: lista tecnologias
# ══════════════════════════════════════════════════════════

def handle_lista_tecnologias() -> dict:
    techs = _carregar_tecnologias()
    return {
        "status": 200,
        "total": len(techs),
        "tecnologias": [
            {"id": t["id"], "nome": t["nome"], "categoria": t["categoria"],
             "nivel": t["nivel"], "modulos": t["numero_de_modulos"],
             "xp": t["xp_total"], "carga": t["carga_horaria_total"]}
            for t in techs
        ],
    }
