# 📘 Documentação Técnica Completa — GEO Explorer

> **Versão:** 1.0.0 | **Autor:** Hitalo Silva | **Repositório:** https://github.com/hitalosilva412-debug/Geo-Explorer

---

## 📋 Índice

1. [Arquitetura do Sistema](#1-arquitetura-do-sistema)
2. [Estrutura de Pastas](#2-estrutura-de-pastas)
3. [Dados — Schemas](#3-dados--schemas)
4. [Slash Commands — Referência Completa](#4-slash-commands--referência-completa)
5. [MCP Service — API REST](#5-mcp-service--api-rest)
6. [Autenticação](#6-autenticação)
7. [Testes Automatizados](#7-testes-automatizados)
8. [Configuração e Variáveis de Ambiente](#8-configuração-e-variáveis-de-ambiente)
9. [Fluxos de Uso](#9-fluxos-de-uso)
10. [Dicas para Profissionais](#10-dicas-para-profissionais)
11. [Roadmap](#11-roadmap)
12. [Glossário](#12-glossário)

---

## 1. Arquitetura do Sistema

```
┌──────────────────────────────────────────────────────┐
│                   GEO Explorer v1.0.0                │
│                                                      │
│  ┌─────────────────┐    ┌──────────────────────────┐ │
│  │  Slash Commands │    │     MCP Service          │ │
│  │  (Bob Chat)     │    │   (HTTP :8090)           │ │
│  │                 │    │                          │ │
│  │ /geo            │    │ GET /api/v1/geo           │ │
│  │ /mapa           │    │ GET /api/v1/trilha_geo    │ │
│  │ /trilha_geo     │    │ GET /api/v1/desafio_geo   │ │
│  │ /desafio_geo    │    │ POST /api/v1/certificado  │ │
│  │ /certificado_geo│    │ POST /api/v1/auth/token   │ │
│  └────────┬────────┘    └────────────┬─────────────┘ │
│           │                          │               │
│           └──────────┬───────────────┘               │
│                      ▼                               │
│           ┌──────────────────────┐                   │
│           │      handlers.py     │                   │
│           │  (lógica de negócio) │                   │
│           └──────────┬───────────┘                   │
│                      │                               │
│         ┌────────────┴────────────┐                  │
│         ▼                        ▼                   │
│  ┌─────────────┐       ┌──────────────────────┐      │
│  │paises       │       │ tecnologias          │      │
│  │.geo_json    │       │ .geo_json            │      │
│  │15 países    │       │ 20 tecnologias       │      │
│  └─────────────┘       │ 198 módulos          │      │
│                        └──────────────────────┘      │
└──────────────────────────────────────────────────────┘
```

---

## 2. Estrutura de Pastas

```
Geo-Explorer/
├── README.md                        → Início rápido e visão geral
├── CHANGELOG.md                     → Histórico de versões
├── CONTRIBUTING.md                  → Guia de contribuição
│
└── geo_explorer/
    ├── commands/                    → Slash commands (Bob local)
    │   ├── geo.md                   → /geo <país>
    │   ├── mapa.md                  → /mapa <região>
    │   ├── trilha_geo.md            → /trilha_geo <tecnologia>
    │   ├── desafio_geo.md           → /desafio_geo <tech> <nivel>
    │   └── certificado_geo.md       → /certificado_geo <nome> <tech>
    │
    ├── DATA/                        → Fonte de dados
    │   ├── paises.geo_json          → 15 países com dados completos
    │   ├── tecnologias.geo_json     → 20 tecnologias / 198 módulos
    │   ├── regioes/                 → (planejado) dados por região
    │   └── continentes/             → (planejado) dados por continente
    │
    ├── CRC/                         → Controle de Qualidade
    │   ├── test_geo.py              → 43 testes unitários
    │   ├── test_integration.py      → 40 testes de integração
    │   ├── resultado_testes_geo.txt → Log unitários
    │   ├── resultado_integracao.txt → Log integração
    │   ├── fixtures/                → Dados para testes
    │   └── reports/                 → Relatórios de cobertura
    │
    ├── docs/                        → Documentação
    │   ├── DOCUMENTACAO.md          → Este arquivo
    │   ├── api/                     → Docs da API
    │   ├── guias/                   → Tutoriais
    │   ├── exemplos/                → Exemplos práticos
    │   └── certificados-emitidos/   → Certificados gerados
    │
    ├── MCP/                         → MCP Service
    │   ├── server.py                → Servidor HTTP principal
    │   ├── handlers.py              → Lógica dos endpoints
    │   ├── config.py                → Configurações
    │   ├── middleware/              → (planejado) middlewares
    │   ├── utils/                   → (planejado) utilitários
    │   └── README.md                → Docs do MCP Service
    │
    ├── assets/                      → Recursos estáticos
    │   ├── images/                  → Imagens de países
    │   ├── icons/                   → Ícones da interface
    │   └── maps/                    → Arquivos de mapas
    │
    ├── config/                      → Configurações por ambiente
    │   ├── dev/                     → Desenvolvimento
    │   ├── prod/                    → Produção
    │   └── test/                    → Testes
    │
    ├── scripts/                     → Scripts utilitários
    ├── logs/                        → Logs da aplicação
    └── backup/                      → Backups de dados
```

---

## 3. Dados — Schemas

### 3.1 paises.geo_json

```json
{
  "paises": [
    {
      "id": 1,
      "nome": "Brasil",
      "capital": "Brasília",
      "continente": "América do Sul",
      "area_km2": 8515767,
      "populacao": 214000000,
      "idioma": "Português",
      "moeda": "Real (BRL)",
      "fronteiras": ["Argentina", "Bolívia", "..."],
      "pontos_turisticos": ["Cristo Redentor", "..."],
      "curiosidades": ["Maior país da América do Sul", "..."],
      "nivel": "Iniciante",
      "xp": 300
    }
  ]
}
```

**15 países disponíveis:**

| ID | País | Continente | Nível | XP |
|----|------|-----------|-------|-----|
| 1 | Brasil | América do Sul | Iniciante | 300 |
| 2 | Argentina | América do Sul | Iniciante | 300 |
| 3 | França | Europa | Intermediário | 500 |
| 4 | Japão | Ásia | Intermediário | 500 |
| 5 | Egito | África | Intermediário | 500 |
| 6 | Austrália | Oceania | Avançado | 800 |
| 7 | Canadá | América do Norte | Intermediário | 500 |
| 8 | China | Ásia | Avançado | 800 |
| 9 | Índia | Ásia | Avançado | 800 |
| 10 | México | América do Norte | Iniciante | 300 |
| 11 | Rússia | Europa/Ásia | Avançado | 800 |
| 12 | Itália | Europa | Intermediário | 500 |
| 13 | EUA | América do Norte | Iniciante | 300 |
| 14 | África do Sul | África | Avançado | 800 |
| 15 | Noruega | Europa | Avançado | 800 |

### 3.2 tecnologias.geo_json

```json
{
  "tecnologias": [
    {
      "id": 1,
      "nome": "GeoMapping com Python",
      "categoria": "Dados Geográficos",
      "nivel": "Iniciante",
      "numero_de_modulos": 6,
      "xp_total": 3200,
      "carga_horaria_total": "24h",
      "badges": ["Map Starter", "Python Geo", "Data Plotter"],
      "promocao_vitalicia": true,
      "certificado_disponivel": true,
      "pre_requisitos": ["Python Básico"],
      "tecnologias_usadas": ["Python", "Folium", "Geopandas"],
      "modulos": [
        {"id": 1, "titulo": "...", "carga": "4h", "xp": 400, "tipo": "teoria"},
        {"id": 6, "titulo": "Projeto Final — ...", "carga": "3h", "xp": 600, "tipo": "projeto"}
      ],
      "lives": ["Live: ...", "Live: ...", "Live: ..."]
    }
  ]
}
```

**20 tecnologias disponíveis:**

| # | Tecnologia | Categoria | Nível | Módulos | XP |
|---|-----------|-----------|-------|---------|-----|
| 1 | GeoMapping com Python | Dados Geográficos | Iniciante | 6 | 3.200 |
| 2 | QGIS | SIG / GIS | Intermediário | 9 | 6.800 |
| 3 | Google Earth Engine | Satélite | Avançado | 11 | 10.500 |
| 4 | Cartografia Digital | Cartografia | Iniciante | 7 | 4.100 |
| 5 | PostGIS | Banco de Dados | Intermediário | 10 | 8.200 |
| 6 | APIs Web Geo | Dev Web | Intermediário | 8 | 6.500 |
| 7 | ML Geoespacial | IA | Avançado | 12 | 12.000 |
| 8 | Climatologia | Clima | Iniciante | 7 | 3.800 |
| 9 | Geopolítica | Geopolítica | Intermediário | 8 | 5.900 |
| 10 | Geodésia | Topografia | Intermediário | 9 | 7.100 |
| 11 | Geomarketing | Negócios | Iniciante | 7 | 4.400 |
| 12 | Ecologia GIS | Meio Ambiente | Intermediário | 9 | 7.200 |
| 13 | Agricultura Precisão | Agronegócio | Avançado | 11 | 10.800 |
| 14 | Drones e Fotogrametria | Topografia | Intermediário | 9 | 7.400 |
| 15 | GPS Avançado | Navegação | Avançado | 10 | 9.600 |
| 16 | Oceanografia | Oceanografia | Avançado | 11 | 10.200 |
| 17 | Infraestrutura Espacial | DevOps | Avançado | 12 | 11.800 |
| 18 | Urbanismo | Urbanismo | Intermediário | 10 | 8.000 |
| 19 | AR Geoespacial | AR / XR | Avançado | 11 | 11.500 |
| 20 | Geografia Física | Geo Física | Iniciante | 6 | 3.100 |

---

## 4. Slash Commands — Referência Completa

### `/geo <país>`
Exibe relatório geográfico completo do país solicitado.
- **Busca:** parcial, case-insensitive
- **Fonte:** `DATA/paises.geo_json`
- **Retorna:** dados, pontos turísticos, curiosidades, plano de visita 5 dias

### `/mapa <região>`
Gera representação visual ASCII da região com legenda e coordenadas.
- **Entrada:** nome de país, continente ou região
- **Retorna:** ASCII art, legenda, hidrografia, relevo, clima

### `/trilha_geo <tecnologia>`
Plano de estudo completo baseado nos módulos da tecnologia.
- **Busca:** parcial no nome e categoria
- **Fonte:** `DATA/tecnologias.geo_json`
- **Retorna:** cronograma semanal, fases, pré-requisitos, lives, dicas

### `/desafio_geo <tecnologia> <nivel>`
Desafio técnico geoespacial com cenário narrativo.
- **Níveis:** Iniciante (200 XP) / Intermediário (500 XP) / Avançado (1000 XP)
- **Retorna:** cenário, enunciado, casos de teste, dicas, solução comentada

### `/certificado_geo <nome> <tecnologia>`
Certificado fictício em Markdown com ID único.
- **Salva em:** `docs/certificados-emitidos/cert-<nome>-<data>.md`
- **Retorna:** certificado completo com badges, lives e link de verificação

---

## 5. MCP Service — API REST

### Iniciar o servidor

```bash
cd geo_explorer/MCP

python server.py                    # padrão (8090, apikey)
python server.py --port 9090        # porta customizada
python server.py --auth none        # sem autenticação
python server.py --auth sso         # SSO JWT
```

### Endpoints detalhados

#### `GET /api/v1/trilha_geo?tech=X`
```json
{
  "status": 200,
  "trilha": {
    "id": 2, "nome": "QGIS", "nivel": "Intermediário",
    "modulos": 9, "xp_total": 6800, "carga_horaria": "42h",
    "badges": ["GIS Analyst", "..."], "lives": ["..."]
  },
  "cronograma": [
    {"semana": 1, "modulo": 1, "titulo": "...", "tipo": "teoria", "carga": "4h", "xp": 500}
  ],
  "total_semanas": 5,
  "fases": {"teoria": 3, "pratica": 5, "projeto": 1}
}
```

#### `POST /api/v1/certificado_geo`
```json
// Request body:
{"nome": "Hitalo Silva", "tecnologia": "QGIS"}

// Response:
{
  "status": 201,
  "certificado": {
    "id": "GEO-2026-XXXXXXXX",
    "usuario": "Hitalo Silva",
    "tecnologia": "Análise de Dados Geográficos com QGIS",
    "xp": 6800,
    "badges": ["GIS Analyst", "QGIS Master", "Spatial Thinker"],
    "arquivo": "geo_explorer/docs/certificados-emitidos/cert-hitalo-silva-20260819.md",
    "verificacao": "https://geoexplorer.app/certificate/GEO-2026-XXXXXXXX"
  }
}
```

---

## 6. Autenticação

| Modo | Header | Chaves de teste |
|------|--------|----------------|
| `apikey` | `X-API-Key: geo-dev-key-001` | `geo-dev-key-001`, `geo-dev-key-002` |
| `sso` | `Authorization: Bearer <JWT>` | Gerado via `POST /api/v1/auth/token` |
| `none` | — | Apenas para desenvolvimento |

---

## 7. Testes Automatizados

### Executar

```bash
cd geo_explorer/CRC

# Unitários (43 testes)
python test_geo.py
# → resultado_testes_geo.txt

# Integração (40 testes)
python test_integration.py
# → resultado_integracao.txt
```

### Cobertura atual

| Arquivo | Suites | Testes | Cobertura |
|---------|--------|--------|-----------|
| `test_geo.py` | 7 | 43 | ✅ 100% |
| `test_integration.py` | 4 | 40 | ✅ 100% |
| **Total** | **11** | **83** | **✅ 100%** |

---

## 8. Configuração e Variáveis de Ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `GEO_HOST` | `0.0.0.0` | Host do servidor |
| `GEO_PORT` | `8090` | Porta |
| `GEO_AUTH_MODE` | `apikey` | Modo: none / apikey / sso |
| `GEO_API_KEYS` | `geo-dev-key-001,...` | Chaves válidas |
| `GEO_SSO_SECRET` | `geo-sso-secret-2026` | Secret JWT |

---

## 9. Fluxos de Uso

### Fluxo Aluno

```
/trilha_geo QGIS
  → Recebe cronograma de 9 módulos em 5 semanas

/desafio_geo QGIS Iniciante
  → Recebe desafio: "Carregue um GeoJSON e exiba atributos"

/desafio_geo QGIS Intermediário
  → Recebe desafio de análise espacial com buffer

/certificado_geo "João Silva" QGIS
  → Recebe certificado com ID GEO-2026-XXXXXXXX
  → Arquivo salvo em docs/certificados-emitidos/
```

### Fluxo via API

```bash
# 1. Autenticar
TOKEN=$(curl -s -X POST http://localhost:8090/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{"usuario":"hitalo"}' | python -c "import sys,json; print(json.load(sys.stdin)['token'])")

# 2. Buscar trilha
curl -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8090/api/v1/trilha_geo?tech=QGIS"

# 3. Gerar certificado
curl -X POST http://localhost:8090/api/v1/certificado_geo \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nome":"Hitalo","tecnologia":"QGIS"}'
```

---

## 10. Dicas para Profissionais

- 🔐 **Produção:** use `GEO_AUTH_MODE=sso` e `GEO_SSO_SECRET` forte (32+ chars)
- 📦 **Extensão:** adicione dados em `*.geo_json` — sem alterar código
- 🧪 **CI/CD:** adicione `python test_geo.py && python test_integration.py` no pipeline
- 🐳 **Docker:** `FROM python:3.11-slim` + `COPY . . && python server.py`
- 🌐 **CORS:** já habilitado com `Access-Control-Allow-Origin: *`

---

## 11. Roadmap

- [ ] v1.1.0 — SQLite + Dashboard web
- [ ] v1.2.0 — Progresso do aluno por tecnologia
- [ ] v2.0.0 — Docker + GitHub Actions + OAuth2 real + Deploy cloud

---

## 12. Glossário

| Termo | Definição |
|-------|-----------|
| **GIS** | Geographic Information System — sistema de informação geográfica |
| **MCP** | Model Context Protocol — serviço de API local |
| **Slash Command** | Comando `/` executado no chat do Bob |
| **JWT** | JSON Web Token — autenticação stateless |
| **QGIS** | Software livre de SIG desktop |
| **GeoJSON** | Formato padrão para dados geoespaciais em JSON |
| **XP** | Experience Points — pontos de experiência |
| **Badge** | Conquista desbloqueada ao completar etapas |

---

> 📌 GEO Explorer v1.0.0 — Hitalo Silva — 2026
> 🌍 _Explore o Mundo através dos Dados_
