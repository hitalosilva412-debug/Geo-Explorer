# 💾 backup/

Backups automáticos do GEO Explorer.

```
backup/
├── data/          → Backups dos arquivos JSON de dados
└── certificados/  → Backups dos certificados emitidos
```

## Convenção de nomes

```
backup/data/paises_2026-08-19.json
backup/certificados/certs_2026-08-19.tar.gz
```

## Executar backup manual

```bash
python scripts/backup.py --full
python scripts/backup.py --only data
python scripts/backup.py --only certificados
```

> ⚠️ Backups são ignorados pelo `.gitignore` em produção
