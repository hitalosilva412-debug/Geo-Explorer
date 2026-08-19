# 🌍 GEO Explorer

> **Plataforma educacional de exploração geográfica** — dados, trilhas de estudo, desafios técnicos e certificados fictícios com API REST integrada.

---

## 🧭 O que é o GEO Explorer?

O **GEO Explorer** é uma plataforma educacional fictícia criada para ensinar e explorar o mundo da **geotecnologia**, da **geografia** e das **tecnologias de informação geográfica (GIS)** de forma prática e interativa.

Ele foi desenvolvido como um projeto de aprendizado que simula um ecossistema educacional completo, inspirado em plataformas como a [DIO](https://www.dio.me/), mas com foco total em **dados geoespaciais e geografia**.

### 🎯 O que você pode fazer com ele?

- 🌍 **Explorar países** — acesse dados detalhados de 15 países: capital, área, população, fronteiras, pontos turísticos e curiosidades
- 🗺️ **Visualizar mapas** — gere representações ASCII de regiões do mundo com legenda, relevo e hidrografia
- 📚 **Estudar geotecnologias** — acesse planos de estudo com cronograma semanal para 20 tecnologias como QGIS, Python, Google Earth Engine, PostGIS, Drones e muito mais
- 💻 **Resolver desafios** — receba desafios técnicos geoespaciais personalizados por tecnologia e nível (Iniciante, Intermediário ou Avançado)
- 🏆 **Conquistar certificados** — gere certificados fictícios em Markdown com ID único, badges e link de verificação
- 📡 **Integrar via API** — consuma todos os recursos através de uma API REST com autenticação por API Key ou SSO JWT

### 🧱 Como ele é estruturado?

O projeto é composto por **4 pilares principais:**

| Pilar | Descrição |
|-------|-----------|
| 🎯 **Slash Commands** | Comandos `/geo`, `/mapa`, `/trilha_geo`, `/desafio_geo` e `/certificado_geo` usados diretamente no chat do Bob |
| 📊 **Dados** | Dois arquivos JSON com 15 países e 20 tecnologias geoespaciais (198 módulos) |
| 📡 **MCP Service** | Servidor HTTP local (porta 8090) com 10 endpoints REST protegidos por autenticação |
| 🧪 **Testes** | 83 testes automatizados (43 unitários + 40 de integração) com 100% de cobertura |

### 👥 Para quem é?

- 🎓 **Estudantes** de geografia, geoprocessamento e geotecnologias
- 👨‍💻 **Desenvolvedores** que querem aprender a construir APIs REST com Python puro
- 🏫 **Educadores** que precisam de exemplos práticos de plataformas educacionais
- 🔬 **Pesquisadores** que querem um template de projeto com dados geoespaciais fictícios

[![Testes](https://img.shields.io/badge/testes-83%2F83-brightgreen)](geo_explorer/CRC/)
[![Cobertura](https://img.shields.io/badge/cobertura-100%25-brightgreen)](geo_explorer/CRC/)
[![Versão](https://img.shields.io/badge/versão-1.0.0-blue)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![Licença](https://img.shields.io/badge/licença-MIT-green)](LICENSE)

---

## 📋 Índice

- [O que é o GEO Explorer](#-o-que-é-o-geo-explorer)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Visão Geral](#-visão-geral)
- [Início Rápido](#-início-rápido)
- [Slash Commands](#-slash-commands)
- [API REST — MCP Service](#-api-rest--mcp-service)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Dados](#-dados)
- [Testes](#-testes)
- [Documentação Completa](#-documentação-completa)

---

## 🚀 Como Executar o Projeto

### ✅ Pré-requisitos

Antes de começar, certifique-se de ter instalado:

| Requisito | Versão mínima | Download |
|-----------|--------------|---------|
| **Python** | 3.10+ | [python.org](https://www.python.org/downloads/) |
| **Git** | 2.30+ | [git-scm.com](https://git-scm.com/) |

> Nenhuma dependência externa é necessária — o servidor usa apenas a **biblioteca padrão do Python**.

---

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/hitalosilva412-debug/Geo-Explorer.git
cd Geo-Explorer
```

---

### 2️⃣ Inicie o MCP Service (API REST)

```bash
cd geo_explorer/MCP

# Modo padrão — porta 8090, autenticação por API Key
python server.py
```

Você verá o banner de confirmação:

```
╔══════════════════════════════════════════════╗
║     🌍 GEO Explorer MCP Service v1.0.0       ║
╚══════════════════════════════════════════════╝
  🌐 http://localhost:8090  |  Auth: apikey
```

#### Opções de inicialização

```bash
# Porta customizada
python server.py --port 9090

# Sem autenticação (desenvolvimento local)
python server.py --auth none

# Modo SSO com JWT
python server.py --auth sso
```

---

### 3️⃣ Teste se está funcionando

```bash
# Health check — sem autenticação
curl http://localhost:8090/

# Listar países — com API Key
curl -H "X-API-Key: geo-dev-key-001" \
  http://localhost:8090/api/v1/paises

# Plano de estudo QGIS
curl -H "X-API-Key: geo-dev-key-001" \
  "http://localhost:8090/api/v1/trilha_geo?tech=QGIS"

# Gerar certificado
curl -X POST http://localhost:8090/api/v1/certificado_geo \
  -H "X-API-Key: geo-dev-key-001" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Seu Nome", "tecnologia": "QGIS"}'
```

---

### 4️⃣ Use os Slash Commands no Bob

Com o projeto aberto no Bob, use diretamente no chat:

```
/geo Brasil
/mapa América do Sul
/trilha_geo QGIS
/desafio_geo Python Avançado
/certificado_geo SeuNome QGIS
```

> ⚠️ Os slash commands ficam em `.bob/commands/` e são **locais ao workspace**.

---

### 5️⃣ Execute os Testes Automatizados

```bash
cd geo_explorer/CRC

# Testes unitários (43 testes)
python test_geo.py

# Testes de integração (40 testes)
python test_integration.py
```

Resultado esperado:
```
✅ Testes: 43/43 | Cobertura: 100.0%
✅ Testes: 40/40 | Cobertura: 100.0%
```

---

### ⚙️ Variáveis de Ambiente (opcional)

Copie o arquivo de exemplo e ajuste conforme necessário:

```bash
cp geo_explorer/MCP/.env.example geo_explorer/MCP/.env
```

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `GEO_HOST` | `0.0.0.0` | Host do servidor |
| `GEO_PORT` | `8090` | Porta do servidor |
| `GEO_AUTH_MODE` | `apikey` | Modo de autenticação |
| `GEO_API_KEYS` | `geo-dev-key-001,...` | Chaves de API válidas |
| `GEO_SSO_SECRET` | `geo-sso-secret-2026` | Secret para JWT |

---

## 🎯 Visão Geral

O **GEO Explorer** combina:

```
📚 Educação Geográfica   →  15 países + 20 tecnologias geoespaciais
🎯 Slash Commands        →  /trilha_geo /desafio_geo /certificado_geo /geo /mapa
📡 API REST              →  8 endpoints com auth APIKey / SSO JWT
🧪 Testes Automatizados  →  83 testes · 100% cobertura
📜 Certificados          →  Gerados e salvos em Markdown
```

---

## ⚡ Início Rápido

```bash
# 1. Clone o repositório
git clone https://github.com/hitalosilva412-debug/Geo-Explorer.git
cd Geo-Explorer

# 2. Inicie o MCP Service
cd geo_explorer/MCP
python server.py

# 3. Teste no navegador ou curl
curl http://localhost:8090/
curl -H "X-API-Key: geo-dev-key-001" http://localhost:8090/api/v1/paises
```

---

## 🎯 Slash Commands

> Use diretamente no **chat do Bob**. Comandos locais em `.bob/commands/`.

| Comando | Exemplo | Resultado |
|---------|---------|-----------|
| `/geo` | `/geo Brasil` | Relatório geográfico completo + plano de visita |
| `/mapa` | `/mapa América do Sul` | Mapa ASCII com legenda e pontos de referência |
| `/trilha_geo` | `/trilha_geo QGIS` | Plano de estudo com cronograma semanal |
| `/desafio_geo` | `/desafio_geo Python Avançado` | Desafio técnico com casos de teste e solução |
| `/certificado_geo` | `/certificado_geo Hitalo QGIS` | Certificado fictício em Markdown |

---

## 📡 API REST — MCP Service

**Base URL:** `http://localhost:8090`

### Endpoints

| Método | Rota | Auth | Descrição |
|--------|------|------|-----------|
| `GET` | `/` | ❌ | Health check |
| `GET` | `/api/v1/status` | ❌ | Status e versão |
| `GET` | `/api/v1/docs` | ❌ | Documentação JSON |
| `POST` | `/api/v1/auth/token` | ❌ | Gerar token SSO |
| `GET` | `/api/v1/paises` | ✅ | Listar 15 países |
| `GET` | `/api/v1/tecnologias` | ✅ | Listar 20 tecnologias |
| `GET` | `/api/v1/geo?pais=X` | ✅ | Dados de um país |
| `GET` | `/api/v1/trilha_geo?tech=X` | ✅ | Plano de estudo |
| `GET` | `/api/v1/desafio_geo?tech=X&nivel=Y` | ✅ | Desafio de código |
| `POST` | `/api/v1/certificado_geo` | ✅ | Gerar certificado |

### Autenticação

```bash
# API Key (padrão)
curl -H "X-API-Key: geo-dev-key-001" http://localhost:8090/api/v1/paises

# SSO — gerar token
curl -X POST http://localhost:8090/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{"usuario": "hitalo"}'

# SSO — usar token
curl -H "Authorization: Bearer <token>" http://localhost:8090/api/v1/paises
```

### Exemplos

```bash
# Plano de estudo — QGIS
curl -H "X-API-Key: geo-dev-key-001" \
  "http://localhost:8090/api/v1/trilha_geo?tech=QGIS"

# Desafio Python Avançado
curl -H "X-API-Key: geo-dev-key-001" \
  "http://localhost:8090/api/v1/desafio_geo?tech=Python&nivel=Avan%C3%A7ado"

# Gerar certificado
curl -X POST http://localhost:8090/api/v1/certificado_geo \
  -H "X-API-Key: geo-dev-key-001" \
  -H "Content-Type: application/json" \
  -d '{"nome": "Hitalo Silva", "tecnologia": "QGIS"}'
```

---

## 📁 Estrutura do Projeto

```
Geo-Explorer/
│
├── README.md                         → Este arquivo
├── CHANGELOG.md                      → Histórico de versões
├── CONTRIBUTING.md                   → Guia de contribuição
│
└── geo_explorer/
    │
    ├── commands/                     → Slash commands do Bob
    │   ├── geo.md                    → /geo <país>
    │   ├── mapa.md                   → /mapa <região>
    │   ├── trilha_geo.md             → /trilha_geo <tecnologia>
    │   ├── desafio_geo.md            → /desafio_geo <tech> <nivel>
    │   └── certificado_geo.md        → /certificado_geo <nome> <tech>
    │
    ├── DATA/                         → Dados geográficos e educacionais
    │   ├── paises.geo_json           → 15 países com dados completos
    │   └── tecnologias.geo_json      → 20 tecnologias com 198 módulos
    │
    ├── CRC/                          → Controle de Qualidade
    │   ├── test_geo.py               → 43 testes unitários
    │   ├── test_integration.py       → 40 testes de integração
    │   ├── resultado_testes_geo.txt  → Log testes unitários
    │   └── resultado_integracao.txt  → Log testes integração
    │
    ├── docs/                         → Documentação e certificados
    │   ├── DOCUMENTACAO.md           → Documentação técnica completa
    │   └── certificados-emitidos/    → Certificados gerados
    │
    ├── MCP/                          → API REST (MCP Service)
    │   ├── server.py                 → Servidor HTTP (porta 8090)
    │   ├── handlers.py               → Lógica de negócio
    │   ├── config.py                 → Configurações
    │   └── README.md                 → Docs do MCP Service
    │
    ├── assets/                       → Recursos estáticos
    ├── config/                       → Configurações por ambiente
    ├── scripts/                      → Scripts utilitários
    ├── logs/                         → Logs da aplicação
    └── backup/                       → Backups de dados
```

---

## 📊 Dados

### paises.geo_json — 15 países

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | string | Nome do país |
| `capital` | string | Capital |
| `continente` | string | Continente |
| `area_km2` | int | Área em km² |
| `populacao` | int | População |
| `fronteiras` | array | Países fronteiriços |
| `pontos_turisticos` | array | Atrações principais |
| `curiosidades` | array | Fatos interessantes |
| `nivel` | string | Iniciante / Intermediário / Avançado |
| `xp` | int | XP ao completar |

### tecnologias.geo_json — 20 tecnologias / 198 módulos

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `nome` | string | Nome da tecnologia |
| `categoria` | string | Área de conhecimento |
| `nivel` | string | Dificuldade |
| `numero_de_modulos` | int | Quantidade de módulos |
| `xp_total` | int | XP total da trilha |
| `carga_horaria_total` | string | Carga em horas |
| `modulos` | array | Lista de módulos com título, carga, xp, tipo |
| `badges` | array | Badges disponíveis |
| `lives` | array | Lives recomendadas |
| `pre_requisitos` | array | Pré-requisitos |

---

## 🧪 Testes

```bash
# Testes unitários (43 testes)
cd geo_explorer/CRC
python test_geo.py

# Testes de integração (40 testes)
python test_integration.py
```

**Resultado atual:**
```
Unitários  : 43/43  ✅  100%
Integração : 40/40  ✅  100%
TOTAL      : 83/83  ✅  100%
```

---

## 📖 Documentação Completa

👉 [`geo_explorer/docs/DOCUMENTACAO.md`](geo_explorer/docs/DOCUMENTACAO.md)

---

## 🤝 Contribuição

Veja o guia em [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

> 🌍 **GEO Explorer v1.0.0** — _Explore o Mundo através dos Dados_
> Projeto fictício educacional | [Hitalo Silva](https://github.com/hitalosilva412-debug)
