"""
=============================================================
  GEO Explorer — MCP Service
  handlers.py — Lógica dos endpoints
=============================================================
"""
import json, os, random
from datetime import datetime
from config import PAISES_JSON, CERTS_DIR


def _carregar_paises():
    with open(PAISES_JSON, encoding="utf-8-sig") as f:
        return json.load(f)["paises"]

def _buscar_pais(nome):
    for p in _carregar_paises():
        if nome.lower() in p["nome"].lower():
            return p
    return None


def handle_geo(pais_nome: str) -> dict:
    if not pais_nome:
        return {"status": 400, "erro": "Parâmetro 'pais' obrigatório"}
    pais = _buscar_pais(pais_nome)
    if not pais:
        return {"status": 404, "erro": f"País '{pais_nome}' não encontrado",
                "sugestoes": [p["nome"] for p in _carregar_paises()]}
    return {"status": 200, "pais": pais}


def handle_desafio_geo(tema: str, nivel: str = "Intermediário") -> dict:
    if not tema:
        return {"status": 400, "erro": "Parâmetro 'tema' obrigatório"}
    niveis = {"iniciante": ("Iniciante", 100, "5min"),
              "intermediario": ("Intermediário", 300, "10min"),
              "intermediário": ("Intermediário", 300, "10min"),
              "avancado": ("Avançado", 600, "20min"),
              "avançado": ("Avançado", 600, "20min")}
    n = niveis.get(nivel.lower(), ("Intermediário", 300, "10min"))
    questoes = {
        "iniciante": [
            "Qual é a capital do Brasil?",
            "Em qual continente fica o Egito?",
            "Qual é o maior país do mundo?",
        ],
        "intermediário": [
            f"Quais países fazem fronteira com {tema}?",
            f"Qual é o idioma oficial de {tema}?",
            f"Qual é a moeda utilizada em {tema}?",
        ],
        "avançado": [
            f"Descreva a geopolítica de {tema} nos últimos 50 anos.",
            f"Compare o PIB de {tema} com a média regional.",
            f"Quais são os principais desafios ambientais de {tema}?",
        ],
    }
    q = questoes.get(n[0].lower().replace("á","a").replace("é","e"), questoes["intermediário"])
    return {
        "status": 200,
        "desafio": {
            "tema": tema, "nivel": n[0], "xp": n[1],
            "tempo": n[2], "questoes": q,
            "titulo": f"Desafio GEO — {tema} | {n[0]}",
        }
    }


def handle_certificado_geo(nome: str, tema: str) -> dict:
    if not nome or not tema:
        return {"status": 400, "erro": "Parâmetros 'nome' e 'tema' obrigatórios"}
    pais = _buscar_pais(tema)
    xp   = pais["xp"] if pais else 300
    nivel = pais["nivel"] if pais else "Intermediário"
    cert_id  = f"GEO-2026-{abs(hash(nome+tema)) % 99999999:08d}"
    data     = datetime.now().strftime("%d/%m/%Y")
    conteudo = f"""# 🌍 CERTIFICADO DE EXPLORAÇÃO GEOGRÁFICA

## ✨ {nome.upper()} ✨

Completou com distinção a exploração de:

## 🌐 {tema}

| Campo | Detalhes |
|-------|----------|
| 🌍 Tema | {tema} |
| 📊 Nível | {nivel} |
| ⭐ XP | {xp} XP |
| 📅 Data | {data} |
| 🆔 ID | {cert_id} |

> 🔒 https://geoexplorer.app/certificate/{cert_id}
_GEO Explorer v1.0.0 — Certificado Fictício_
"""
    os.makedirs(CERTS_DIR, exist_ok=True)
    slug = nome.lower().replace(" ","-")
    path = os.path.join(CERTS_DIR, f"cert-{slug}-{datetime.now().strftime('%Y%m%d')}.md")
    with open(path,"w",encoding="utf-8") as f: f.write(conteudo)
    return {"status": 201, "certificado": {"id": cert_id, "usuario": nome,
            "tema": tema, "xp": xp, "data": data, "arquivo": path}}


def handle_lista_paises() -> dict:
    paises = _carregar_paises()
    return {"status": 200, "total": len(paises),
            "paises": [{"id":p["id"],"nome":p["nome"],"capital":p["capital"],
                        "continente":p["continente"],"nivel":p["nivel"],"xp":p["xp"]} for p in paises]}
