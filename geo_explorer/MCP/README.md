# 📡 MCP/ — MCP Service

Servidor HTTP da API REST do GEO Explorer.

```
MCP/
├── server.py        → Servidor HTTP principal (porta 8090)
├── handlers.py      → Lógica de negócio dos endpoints
├── config.py        → Configurações e variáveis de ambiente
├── middleware/      → Middlewares (auth, rate limit, cors, logging)
└── utils/           → Utilitários auxiliares
```

## Endpoints

| Método | Rota | Auth | Descrição |
|--------|------|------|-----------|
| GET | `/` | ❌ | Health check |
| GET | `/api/v1/status` | ❌ | Status do serviço |
| GET | `/api/v1/docs` | ❌ | Documentação |
| GET | `/api/v1/paises` | ✅ | Lista países |
| GET | `/api/v1/geo?pais=X` | ✅ | Dados do país |
| GET | `/api/v1/desafio_geo?tema=X&nivel=Y` | ✅ | Desafio |
| POST | `/api/v1/certificado_geo` | ✅ | Certificado |
| POST | `/api/v1/auth/token` | ❌ | Token SSO |

## Iniciar

```bash
cd geo_explorer/MCP

# Padrão (porta 8090, auth: apikey)
python server.py

# Porta customizada
python server.py --port 9090

# Sem autenticação (dev)
python server.py --auth none
```

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `GEO_HOST` | `0.0.0.0` | Host |
| `GEO_PORT` | `8090` | Porta |
| `GEO_AUTH_MODE` | `apikey` | Modo auth |
| `GEO_API_KEYS` | `geo-dev-key-001,...` | Chaves válidas |
| `GEO_SSO_SECRET` | `geo-sso-secret-2026` | Secret JWT |
