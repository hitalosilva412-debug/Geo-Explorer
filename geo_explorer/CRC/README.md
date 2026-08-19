# 🧪 CRC/ — Controle e Revisão de Código

Testes unitários e relatórios de qualidade do GEO Explorer.

```
CRC/
├── test_geo.py                  → 22 testes unitários (100% cobertura)
├── resultado_testes_geo.txt     → Log da última execução
├── fixtures/                    → Dados fictícios para os testes
└── reports/                     → Relatórios de cobertura e qualidade
```

## Como executar

```bash
# Todos os testes
cd geo_explorer/CRC
python test_geo.py

# Com relatório de cobertura (requer coverage)
pip install coverage
coverage run test_geo.py
coverage report
coverage html -d reports/coverage_html
```

## Resultado atual

| Suite | Testes | Status |
|-------|--------|--------|
| TestCarregarPaises | 3 | ✅ 3/3 |
| TestHandleGeo | 6 | ✅ 6/6 |
| TestHandleDesafioGeo | 5 | ✅ 5/5 |
| TestHandleCertificadoGeo | 5 | ✅ 5/5 |
| TestHandleListaPaises | 3 | ✅ 3/3 |
| **TOTAL** | **22** | **✅ 100%** |

> 🎯 Meta de cobertura: **70%** | Atual: **100%**
