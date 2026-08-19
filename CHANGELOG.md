# 📋 CHANGELOG — GEO Explorer

Todas as mudanças notáveis deste projeto são documentadas aqui.

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [1.0.0] — 2026-08-19 🎉 Lançamento Inicial

### ✅ Adicionado
- **Repositório** — Criação do projeto no GitHub com estrutura profissional
- **Estrutura de pastas** — `commands/`, `DATA/`, `CRC/`, `docs/`, `MCP/`, `assets/`, `config/`, `scripts/`, `logs/`, `backup/`
- **Dados geográficos** — `paises.geo_json` com 15 países e dados completos
- **Dados de tecnologias** — `tecnologias.geo_json` com 20 tecnologias e 198 módulos detalhados

#### Slash Commands
- `/geo <país>` — Relatório geográfico completo com plano de visita
- `/mapa <região>` — Mapa ASCII com legenda e pontos de referência
- `/trilha_geo <tecnologia>` — Plano de estudo com cronograma semanal
- `/desafio_geo <tech> <nivel>` — Desafio técnico geoespacial com casos de teste
- `/certificado_geo <nome> <tech>` — Certificado fictício em Markdown

#### MCP Service (API REST)
- `GET /` — Health check
- `GET /api/v1/status` — Status do serviço
- `GET /api/v1/docs` — Documentação dos endpoints
- `POST /api/v1/auth/token` — Geração de token SSO JWT
- `GET /api/v1/paises` — Listagem dos 15 países
- `GET /api/v1/tecnologias` — Listagem das 20 tecnologias
- `GET /api/v1/geo?pais=X` — Dados detalhados de um país
- `GET /api/v1/trilha_geo?tech=X` — Plano de estudo com cronograma
- `GET /api/v1/desafio_geo?tech=X&nivel=Y` — Desafio de código aleatório
- `POST /api/v1/certificado_geo` — Geração e salvamento de certificado

#### Autenticação
- Modo `apikey` — Header `X-API-Key`
- Modo `sso` — JWT Bearer Token (simulado)
- Modo `none` — Sem autenticação (desenvolvimento)

#### Testes Automatizados
- `test_geo.py` — 43 testes unitários (100% cobertura)
  - `TestCarregarPaises` — 3 testes
  - `TestCarregarTecnologias` — 5 testes
  - `TestHandleGeo` — 6 testes
  - `TestHandleTrilhaGeo` — 8 testes
  - `TestHandleDesafioGeo` — 8 testes
  - `TestHandleCertificadoGeo` — 8 testes
  - `TestHandleListas` — 5 testes
- `test_integration.py` — 40 testes de integração (100% cobertura)
  - `TestSmokeEndpoints` — 15 testes
  - `TestFluxoCompletoQGIS` — 10 testes
  - `TestFluxoCompletoPython` — 5 testes
  - `TestResiliencia` — 10 testes

#### Documentação
- `README.md` — Documentação principal com início rápido
- `geo_explorer/docs/DOCUMENTACAO.md` — Documentação técnica completa
- `CHANGELOG.md` — Este arquivo
- `CONTRIBUTING.md` — Guia de contribuição
- READMEs em cada pasta do projeto

### 🔧 Configurações
- `.gitignore` — Ignora `__pycache__`, `.env`, `*.log`, `*.pyc`
- `MCP/.env.example` — Exemplo de variáveis de ambiente
- `config/dev/`, `config/prod/`, `config/test/` — Ambientes separados

---

## [Unreleased] — Próximas versões

### 🔮 Planejado para v1.1.0
- [ ] Banco de dados SQLite para persistência
- [ ] Dashboard web em React/HTML
- [ ] Progresso do aluno por tecnologia
- [ ] Novos países e tecnologias

### 🔮 Planejado para v2.0.0
- [ ] OAuth2 real (Google/GitHub)
- [ ] Containerização com Docker
- [ ] CI/CD via GitHub Actions
- [ ] Deploy em cloud (Railway/Render)

---

> 🌍 GEO Explorer — _Explore o Mundo através dos Dados_
