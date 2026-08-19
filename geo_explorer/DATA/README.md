# 📊 DATA/

Arquivos de dados geográficos do GEO Explorer.

```
DATA/
├── paises.geo_json       → 15 países com dados completos
├── regioes/              → Dados por região geográfica
└── continentes/          → Dados agrupados por continente
```

## Schema — paises.geo_json

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

## Arquivos planejados

| Arquivo | Conteúdo |
|---------|----------|
| `paises.geo_json` | ✅ 15 países |
| `regioes/america_sul.json` | Dados da América do Sul |
| `regioes/europa.json` | Dados da Europa |
| `regioes/asia.json` | Dados da Ásia |
| `continentes/continentes.json` | Dados dos 7 continentes |
| `capitais.json` | Lista de todas as capitais |
| `curiosidades.json` | Banco de curiosidades geográficas |
