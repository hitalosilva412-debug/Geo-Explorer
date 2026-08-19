# 📋 logs/

Diretório de logs da aplicação GEO Explorer.

```
logs/
├── app.log         → Log geral da aplicação
├── mcp.log         → Log do MCP Service (requisições HTTP)
├── errors.log      → Erros e exceções
└── access.log      → Acessos à API
```

## Formato de log

```
[2026-08-19 12:00:00] INFO  GET /api/v1/geo?pais=Brasil → 200 (12ms)
[2026-08-19 12:00:01] ERROR handlers.py:42 → País não encontrado: XYZ
```

> ⚠️ Arquivos `.log` são ignorados pelo `.gitignore`
> 📦 Rotacionar logs maiores que 10MB
