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

## 🎯 Slash Commands — Como Usar os Comandos

> Digite os comandos diretamente no **chat do Bob**. Eles ficam armazenados em `.bob/commands/` e são **exclusivos deste projeto**.

---

### 📍 `/geo <país>`

Exibe um relatório geográfico completo do país informado.

```
/geo Brasil
/geo Japão
/geo França
```

**O que retorna:**
- 🏛️ Capital, área, população, idioma e moeda
- 🌐 Lista de países fronteiriços
- 🏛️ Principais pontos turísticos com descrições
- 💡 Curiosidades únicas sobre o país
- 🗓️ Plano de visita sugerido de 5 dias
- 📚 Livros e documentários recomendados

> 💡 **Dica:** a busca é parcial e case-insensitive — `/geo brasil` e `/geo BRASIL` funcionam igualmente.

---

### 🗺️ `/mapa <região>`

Gera uma representação visual ASCII da região com informações geográficas.

```
/mapa América do Sul
/mapa Europa
/mapa Brasil
/mapa Oceania
```

**O que retorna:**
- 🗺️ Mapa ASCII criativo da região com símbolos para oceano, montanhas, floresta e cidades
- 🧭 Legenda dos símbolos utilizados
- 📍 Tabela de pontos de referência com coordenadas aproximadas
- 🌊 Principais rios, lagos e mares
- ⛰️ Relevo — montanhas, planaltos e planícies
- 🌤️ Tipos climáticos da região

---

### 📚 `/trilha_geo <tecnologia>`

Gera um plano de estudo completo para a tecnologia geoespacial escolhida.

```
/trilha_geo QGIS
/trilha_geo Python
/trilha_geo GPS
/trilha_geo Machine Learning
/trilha_geo Drones
```

**O que retorna:**
- 📊 Nível, módulos, XP total e carga horária
- 🏅 Badges disponíveis e pré-requisitos
- 🗓️ **Cronograma semanal** com todos os módulos distribuídos
- 🎯 Objetivos divididos em 3 fases: Fundamentos → Desenvolvimento → Certificação
- 📺 Lives recomendadas da trilha
- 💡 Dicas de estudo

**Tecnologias disponíveis (exemplos):**

| Tecnologia | Nível | Módulos |
|-----------|-------|---------|
| GeoMapping com Python | Iniciante | 6 |
| QGIS | Intermediário | 9 |
| Google Earth Engine | Avançado | 11 |
| PostGIS | Intermediário | 10 |
| Machine Learning Geoespacial | Avançado | 12 |
| Drones e Fotogrametria | Intermediário | 9 |
| GPS Avançado | Avançado | 10 |

> 💡 **Dica:** use busca parcial — `/trilha_geo geo` ou `/trilha_geo cartografia` também funcionam.

---

### 💻 `/desafio_geo <tecnologia> <nivel>`

Gera um desafio técnico geoespacial aleatório personalizado.

```
/desafio_geo QGIS Iniciante
/desafio_geo Python Intermediário
/desafio_geo GPS Avançado
/desafio_geo Machine Learning Avançado
```

**Níveis disponíveis:**

| Nível | Tipo de desafio | Tempo | XP |
|-------|----------------|-------|----|
| `Iniciante` | Operações básicas, primeiros mapas | ~15min | 200 XP |
| `Intermediário` | Análise espacial, scripts, APIs | ~45min | 500 XP |
| `Avançado` | Algoritmos complexos, ML, automação | ~90min | 1000 XP |

**O que retorna:**
- 📋 Cenário narrativo realista (ex: "Você é um analista GIS contratado pela prefeitura...")
- 🗺️ Enunciado técnico detalhado
- 🧪 3 casos de teste: básico, real e edge case
- 💡 3 dicas progressivas sem entregar a solução
- 📊 Critérios de avaliação com pesos
- ✅ Solução comentada passo a passo

> 💡 **Dica:** se não informar o nível, o padrão é **Intermediário**.

---

### 🏆 `/certificado_geo <nome> <tecnologia>`

Gera um certificado fictício em Markdown para o usuário que concluiu uma trilha.

```
/certificado_geo Hitalo QGIS
/certificado_geo "Maria Silva" "GeoMapping com Python"
/certificado_geo João "Machine Learning Geoespacial"
```

**O que retorna:**
- 🏆 Certificado completo com logo ASCII do GEO Explorer
- 📊 Tabela com detalhes: nível, módulos, XP, carga horária, badges e data
- 🏅 Lista de badges conquistadas
- 📺 Lives assistidas na trilha
- 🆔 **ID único** no formato `GEO-2026-XXXXXXXX`
- 🔒 Link de verificação fictício
- 💾 **Arquivo salvo automaticamente** em `docs/certificados-emitidos/`

---

### 🔄 Fluxo Recomendado de Uso

```
1. /trilha_geo QGIS          → entenda o plano completo
2. /desafio_geo QGIS Iniciante   → pratique os fundamentos
3. /desafio_geo QGIS Intermediário → avance nos conceitos
4. /certificado_geo SeuNome QGIS → celebre a conquista!
```

---

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

## 🧪 Como Executar os Testes

O GEO Explorer possui **83 testes automatizados** divididos em dois arquivos, cobrindo desde funções isoladas até fluxos completos fim-a-fim.

---

### 📁 Onde ficam os testes?

```
geo_explorer/CRC/
├── test_geo.py              → 43 testes unitários
├── test_integration.py      → 40 testes de integração
├── resultado_testes_geo.txt → log gerado ao rodar test_geo.py
└── resultado_integracao.txt → log gerado ao rodar test_integration.py
```

---

### 1️⃣ Testes Unitários — `test_geo.py`

Validam cada função isoladamente: carregamento de dados, busca, geração de trilhas, desafios e certificados.

```bash
cd geo_explorer/CRC
python test_geo.py
```

**Saída esperada:**
```
✅ Testes: 43/43 | Cobertura: 100.0% | Log: resultado_testes_geo.txt
```

**Suítes incluídas:**

| Suíte | Testes | O que valida |
|-------|--------|-------------|
| `TestCarregarPaises` | 3 | JSON carrega, tem 15 países, campos obrigatórios |
| `TestCarregarTecnologias` | 5 | JSON carrega, 20 tecnologias, módulos e tipos |
| `TestHandleGeo` | 6 | Busca de país, case-insensitive, 400/404 |
| `TestHandleTrilhaGeo` | 8 | Trilha, cronograma, fases, not found |
| `TestHandleDesafioGeo` | 8 | Nível, XP, enunciado, dicas, critérios |
| `TestHandleCertificadoGeo` | 8 | Emissão, ID, arquivo, badges, 400 |
| `TestHandleListas` | 5 | Lista países e tecnologias, campos resumo |

---

### 2️⃣ Testes de Integração — `test_integration.py`

Validam o sistema de ponta a ponta: endpoints HTTP, fluxos completos e casos extremos.

```bash
cd geo_explorer/CRC
python test_integration.py
```

**Saída esperada:**
```
=================================================================
  GEO Explorer — Resultado dos Testes de Integração
=================================================================
  ✅ Smoke Tests MCP                        15 testes
  ✅ Fluxo Completo — QGIS                  10 testes
  ✅ Fluxo Completo — Python                5 testes
  ✅ Resiliência / Edge Cases               10 testes
=================================================================
  Total    : 40
  ✅ Passou : 40
  Cobertura: 100.0%  |  Meta: 70%
  ✅ META ATINGIDA!
=================================================================
```

**Suítes incluídas:**

| Suíte | Testes | O que valida |
|-------|--------|-------------|
| `TestSmokeEndpoints` | 15 | Health check, auth, 401, 404, todos os endpoints |
| `TestFluxoCompletoQGIS` | 10 | Trilha → desafio → certificado → arquivo gerado |
| `TestFluxoCompletoPython` | 5 | Fases, badges, enunciado, fluxo via API HTTP |
| `TestResiliencia` | 10 | Busca parcial, nível inválido, key inválida, edge cases |

---

### 3️⃣ Rodar todos de uma vez

```bash
cd geo_explorer/CRC
python test_geo.py && python test_integration.py
```

---

### 4️⃣ Ver os logs gerados

Os resultados são salvos automaticamente em arquivos `.txt`:

```bash
# Abrir log de testes unitários
type geo_explorer\CRC\resultado_testes_geo.txt

# Abrir log de integração
type geo_explorer\CRC\resultado_integracao.txt
```

---

### 📊 Resultado Atual

| Arquivo | Testes | Passou | Cobertura | Meta |
|---------|--------|--------|-----------|------|
| `test_geo.py` | 43 | 43 | ✅ 100% | ≥70% |
| `test_integration.py` | 40 | 40 | ✅ 100% | ≥70% |
| **Total** | **83** | **83** | **✅ 100%** | ≥70% |

---

## 🔧 Melhorias Realizadas

Esta seção registra todas as evoluções e melhorias implementadas ao longo do desenvolvimento do GEO Explorer.

---

### 🏗️ v1.0.0 — Estrutura e Base do Projeto

| # | Melhoria | Impacto |
|---|----------|---------|
| 1 | Criação do repositório no GitHub com `.gitignore` profissional | Organização e versionamento desde o início |
| 2 | Estrutura de pastas completa: `commands/`, `DATA/`, `CRC/`, `docs/`, `MCP/`, `assets/`, `config/`, `scripts/`, `logs/`, `backup/` | Separação clara de responsabilidades |
| 3 | README em cada pasta com propósito, formato e exemplos | Facilita onboarding de novos colaboradores |
| 4 | `.gitkeep` em pastas vazias para manter estrutura no git | Evita perda da estrutura em clones |

---

### 📊 v1.0.0 — Dados Geográficos e Educacionais

| # | Melhoria | Impacto |
|---|----------|---------|
| 5 | `paises.geo_json` com **15 países** e 10+ campos por país | Base de dados rica para exploração |
| 6 | `tecnologias.geo_json` com **20 tecnologias** e **198 módulos** detalhados | Conteúdo educacional realista |
| 7 | Cada módulo tipado (`teoria`, `pratica`, `projeto`) | Permite análise por fase de aprendizado |
| 8 | Badges e lives por tecnologia | Gamificação do aprendizado |
| 9 | Campo `pre_requisitos` e `tecnologias_usadas` por trilha | Orientação de carreira mais clara |

---

### 🎯 v1.0.0 — Slash Commands

| # | Melhoria | Impacto |
|---|----------|---------|
| 10 | `/geo` com relatório completo + plano de visita 5 dias | Vai além de simples dados — gera experiência |
| 11 | `/mapa` com ASCII art + coordenadas + relevo + clima | Visualização criativa sem dependências externas |
| 12 | `/trilha_geo` com cronograma semanal por módulo | Plano de estudos prático e acionável |
| 13 | `/desafio_geo` com cenário narrativo realista | Desafios contextualizados, não apenas técnicos |
| 14 | `/certificado_geo` salva arquivo `.md` automaticamente | Certificado persistido, não apenas exibido |
| 15 | Todos os comandos com busca **parcial e case-insensitive** | Melhor experiência do usuário |

---

### 📡 v1.0.0 — MCP Service (API REST)

| # | Melhoria | Impacto |
|---|----------|---------|
| 16 | Servidor HTTP com **biblioteca padrão Python** — zero dependências | Instalação imediata sem `pip install` |
| 17 | Suporte a **3 modos de autenticação**: `none`, `apikey`, `sso` | Flexível para dev e produção |
| 18 | JWT simulado sem bibliotecas externas (`hmac` + `base64`) | Demonstra implementação educacional |
| 19 | CORS habilitado por padrão (`Access-Control-Allow-Origin: *`) | Pronto para consumo por frontends |
| 20 | Endpoint `/api/v1/docs` retorna documentação em JSON | Auto-documentação da API |
| 21 | Novo endpoint `GET /api/v1/tecnologias` adicionado | Lista completa das trilhas via API |
| 22 | Novo endpoint `GET /api/v1/trilha_geo` com cronograma | Trilha acessível via HTTP além do chat |
| 23 | CLI com `--port` e `--auth` para configuração sem editar código | Mais flexibilidade operacional |

---

### 🧪 v1.0.0 — Qualidade e Testes

| # | Melhoria | Impacto |
|---|----------|---------|
| 24 | **43 testes unitários** cobrindo 7 suítes distintas | Confiança em cada função isolada |
| 25 | **40 testes de integração** com fluxo E2E completo | Valida o sistema como um todo |
| 26 | Smoke tests dos 10 endpoints HTTP via roteador | Garante que a API responde corretamente |
| 27 | Testes de resiliência: busca parcial, edge cases, métodos inválidos | Sistema robusto a entradas inesperadas |
| 28 | Logs de teste salvos em `.txt` automaticamente | Rastreabilidade dos resultados |
| 29 | Meta de cobertura: **70%** → resultado: **100%** | Superou a meta em 30 pontos percentuais |

---

### 📖 v1.0.0 — Documentação

| # | Melhoria | Impacto |
|---|----------|---------|
| 30 | `README.md` com badges, início rápido e exemplos `curl` | Profissionalismo e usabilidade imediata |
| 31 | Seção **"O que é o GEO Explorer"** com pilares e público-alvo | Clareza sobre o propósito do projeto |
| 32 | Seção **"Como Executar"** com 5 passos detalhados | Reduz fricção para novos usuários |
| 33 | Seção **"Como Usar os Comandos"** com exemplos e retornos | Referência rápida para todos os comandos |
| 34 | Seção **"Como Executar os Testes"** com saída esperada | Facilita CI/CD e onboarding |
| 35 | `CHANGELOG.md` com histórico completo | Rastreabilidade de versões |
| 36 | `CONTRIBUTING.md` com fluxo, padrões e exemplos de código | Abertura para contribuições externas |
| 37 | `DOCUMENTACAO.md` com arquitetura, schemas e fluxos | Referência técnica completa |
| 38 | READMEs individuais em cada pasta | Documentação granular e contextualizada |

---

### 🔮 Próximas Melhorias Previstas

| Versão | Melhoria Planejada |
|--------|-------------------|
| v1.1.0 | Banco de dados SQLite para persistir certificados e progresso |
| v1.1.0 | Dashboard web (HTML/React) para visualizar trilhas |
| v1.2.0 | Sistema de progresso do aluno por tecnologia |
| v1.2.0 | Novos países e tecnologias no JSON |
| v2.0.0 | Docker + GitHub Actions (CI/CD automático) |
| v2.0.0 | OAuth2 real (Google / GitHub login) |
| v2.0.0 | Deploy em cloud (Railway, Render ou AWS) |

---

## 📖 Documentação Completa

👉 [`geo_explorer/docs/DOCUMENTACAO.md`](geo_explorer/docs/DOCUMENTACAO.md)

---

## 🤝 Contribuição

Veja o guia em [`CONTRIBUTING.md`](CONTRIBUTING.md)

---

> 🌍 **GEO Explorer v1.0.0** — _Explore o Mundo através dos Dados_
> Projeto fictício educacional | [Hitalo Silva](https://github.com/hitalosilva412-debug)
