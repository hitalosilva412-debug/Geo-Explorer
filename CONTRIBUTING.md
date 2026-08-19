# 🤝 Guia de Contribuição — GEO Explorer

Obrigado por contribuir com o GEO Explorer! Este guia explica como participar do projeto.

---

## 📋 Índice

- [Como começar](#como-começar)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Padrões de código](#padrões-de-código)
- [Fluxo de contribuição](#fluxo-de-contribuição)
- [Adicionando dados](#adicionando-dados)
- [Criando novos comandos](#criando-novos-comandos)
- [Testes](#testes)
- [Commits](#commits)

---

## 🚀 Como começar

```bash
# 1. Fork o repositório
# 2. Clone seu fork
git clone https://github.com/SEU_USUARIO/Geo-Explorer.git
cd Geo-Explorer

# 3. Crie uma branch para sua feature
git checkout -b feat/nome-da-feature

# 4. Faça suas alterações

# 5. Execute os testes
cd geo_explorer/CRC
python test_geo.py
python test_integration.py

# 6. Commit e push
git add .
git commit -m "feat: descrição da sua feature"
git push origin feat/nome-da-feature

# 7. Abra um Pull Request
```

---

## 📁 Estrutura do Projeto

| Pasta | O que modificar |
|-------|----------------|
| `geo_explorer/DATA/` | Adicionar países ou tecnologias |
| `geo_explorer/commands/` | Criar novos slash commands |
| `geo_explorer/MCP/handlers.py` | Adicionar lógica de negócio |
| `geo_explorer/MCP/server.py` | Adicionar endpoints |
| `geo_explorer/CRC/` | Escrever testes |
| `geo_explorer/docs/` | Documentação |

---

## 📐 Padrões de Código

### Python
- Use **snake_case** para variáveis e funções
- Docstrings em todas as funções públicas
- Máximo **120 caracteres** por linha
- Handlers sempre retornam `{"status": int, ...}`

```python
# ✅ Bom
def handle_minha_feature(parametro: str) -> dict:
    """Descrição clara da função."""
    if not parametro:
        return {"status": 400, "erro": "Parâmetro obrigatório"}
    return {"status": 200, "resultado": ...}

# ❌ Evitar
def f(p):
    return {"s": 200, "r": ...}
```

### JSON (dados)
- Mantenha o schema existente ao adicionar entradas
- Use **UTF-8** com encoding correto
- IDs devem ser sequenciais e únicos

---

## 🔄 Fluxo de Contribuição

```
fork → branch → código → testes → commit → PR → review → merge
```

### Tipos de branches
```
feat/     → nova funcionalidade
fix/      → correção de bug
docs/     → documentação
test/     → testes
refactor/ → refatoração
data/     → adição de dados
```

---

## 📊 Adicionando Dados

### Novo país em `paises.geo_json`
```json
{
  "id": 16,
  "nome": "Portugal",
  "capital": "Lisboa",
  "continente": "Europa",
  "area_km2": 92212,
  "populacao": 10000000,
  "idioma": "Português",
  "moeda": "Euro (EUR)",
  "fronteiras": ["Espanha"],
  "pontos_turisticos": ["Torre de Belém", "Alfama", "Sintra"],
  "curiosidades": ["...", "...", "..."],
  "nivel": "Iniciante",
  "xp": 300
}
```

### Nova tecnologia em `tecnologias.geo_json`
```json
{
  "id": 21,
  "nome": "Nome da Tecnologia",
  "categoria": "Categoria",
  "nivel": "Iniciante|Intermediário|Avançado",
  "numero_de_modulos": N,
  "xp_total": N,
  "carga_horaria_total": "Xh",
  "badges": ["Badge 1", "Badge 2", "Badge 3"],
  "promocao_vitalicia": true,
  "certificado_disponivel": true,
  "pre_requisitos": ["..."],
  "tecnologias_usadas": ["..."],
  "modulos": [
    {"id": 1, "titulo": "...", "carga": "Xh", "xp": N, "tipo": "teoria|pratica|projeto"}
  ],
  "lives": ["Live: ...", "Live: ...", "Live: ..."]
}
```

---

## 🎯 Criando Novos Slash Commands

1. Crie o arquivo em `.bob/commands/nome_comando.md`
2. Use `$ARGUMENTS` para receber parâmetros
3. Referencie os arquivos de dados com caminho completo
4. Adicione o handler em `geo_explorer/MCP/handlers.py`
5. Registre a rota em `geo_explorer/MCP/server.py`
6. Escreva testes em `geo_explorer/CRC/test_geo.py`

---

## 🧪 Testes

### Regras
- Todo novo handler deve ter **mínimo 5 testes unitários**
- Testes de integração para fluxos E2E
- Meta de cobertura: **≥ 70%** (atual: 100%)
- Rode todos antes de fazer PR

```bash
cd geo_explorer/CRC

# Unitários
python test_geo.py

# Integração
python test_integration.py
```

### Estrutura de teste
```python
class TestMeuNovoHandler(unittest.TestCase):
    def test_caso_sucesso(self):
        r = handle_minha_feature("parametro_valido")
        self.assertEqual(r["status"], 200)

    def test_sem_parametro_retorna_400(self):
        self.assertEqual(handle_minha_feature("")["status"], 400)

    def test_nao_encontrado_retorna_404(self):
        self.assertEqual(handle_minha_feature("xyz_invalido")["status"], 404)
```

---

## 📝 Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: adiciona suporte a novo país
fix: corrige busca case-insensitive
docs: atualiza README com novos exemplos
test: adiciona testes para handle_trilha_geo
data: adiciona 5 novos países europeus
refactor: simplifica lógica do handler de certificado
```

---

## 📬 Reportando Bugs

Abra uma [Issue](https://github.com/hitalosilva412-debug/Geo-Explorer/issues) com:
- Descrição clara do problema
- Passos para reproduzir
- Resultado esperado vs obtido
- Versão do Python e sistema operacional

---

> 🌍 Obrigado por contribuir com o GEO Explorer!
