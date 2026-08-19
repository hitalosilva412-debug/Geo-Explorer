"""
=============================================================
  GEO Explorer — Testes Unitários
  CRC/test_geo.py — Cobertura alvo: >= 70%
=============================================================
"""
import json, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "MCP"))
from handlers import _carregar_paises, _buscar_pais, handle_geo, handle_desafio_geo, handle_certificado_geo, handle_lista_paises


class TestCarregarPaises(unittest.TestCase):
    def test_json_carrega(self):
        self.assertIsInstance(_carregar_paises(), list)
    def test_tem_15_paises(self):
        self.assertEqual(len(_carregar_paises()), 15)
    def test_campos_obrigatorios(self):
        campos = ["id","nome","capital","continente","area_km2","populacao","idioma","moeda","nivel","xp"]
        for p in _carregar_paises():
            for c in campos:
                self.assertIn(c, p)

class TestHandleGeo(unittest.TestCase):
    def test_brasil_encontrado(self):
        r = handle_geo("Brasil")
        self.assertEqual(r["status"], 200)
        self.assertEqual(r["pais"]["nome"], "Brasil")
    def test_busca_case_insensitive(self):
        self.assertEqual(handle_geo("brasil")["status"], 200)
    def test_pais_nao_encontrado(self):
        r = handle_geo("PaisInexistenteXYZ")
        self.assertEqual(r["status"], 404)
    def test_nao_encontrado_retorna_sugestoes(self):
        r = handle_geo("PaisInexistenteXYZ")
        self.assertIn("sugestoes", r)
        self.assertGreater(len(r["sugestoes"]), 0)
    def test_sem_parametro(self):
        self.assertEqual(handle_geo("")["status"], 400)
    def test_japao_encontrado(self):
        r = handle_geo("Japão")
        self.assertEqual(r["status"], 200)

class TestHandleDesafioGeo(unittest.TestCase):
    def test_desafio_brasil_iniciante(self):
        r = handle_desafio_geo("Brasil", "Iniciante")
        self.assertEqual(r["status"], 200)
        self.assertEqual(r["desafio"]["nivel"], "Iniciante")
    def test_desafio_xp_positivo(self):
        r = handle_desafio_geo("França", "Avançado")
        self.assertGreater(r["desafio"]["xp"], 0)
    def test_sem_nivel_usa_intermediario(self):
        r = handle_desafio_geo("Brasil")
        self.assertEqual(r["desafio"]["nivel"], "Intermediário")
    def test_desafio_tem_questoes(self):
        r = handle_desafio_geo("Brasil", "Intermediário")
        self.assertGreater(len(r["desafio"]["questoes"]), 0)
    def test_sem_tema_retorna_400(self):
        self.assertEqual(handle_desafio_geo("")["status"], 400)

class TestHandleCertificadoGeo(unittest.TestCase):
    def test_certificado_emitido(self):
        r = handle_certificado_geo("Hitalo Silva", "Brasil")
        self.assertEqual(r["status"], 201)
    def test_certificado_tem_id(self):
        r = handle_certificado_geo("Hitalo", "Brasil")
        self.assertTrue(r["certificado"]["id"].startswith("GEO-2026-"))
    def test_certificado_arquivo_criado(self):
        r = handle_certificado_geo("Hitalo", "Brasil")
        self.assertTrue(os.path.exists(r["certificado"]["arquivo"]))
    def test_sem_nome_retorna_400(self):
        self.assertEqual(handle_certificado_geo("", "Brasil")["status"], 400)
    def test_sem_tema_retorna_400(self):
        self.assertEqual(handle_certificado_geo("Hitalo", "")["status"], 400)

class TestHandleListaPaises(unittest.TestCase):
    def test_lista_retorna_200(self):
        self.assertEqual(handle_lista_paises()["status"], 200)
    def test_lista_tem_15_paises(self):
        self.assertEqual(handle_lista_paises()["total"], 15)
    def test_campos_resumo(self):
        p = handle_lista_paises()["paises"][0]
        for c in ["id","nome","capital","continente","nivel","xp"]:
            self.assertIn(c, p)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    for tc in [TestCarregarPaises, TestHandleGeo, TestHandleDesafioGeo, TestHandleCertificadoGeo, TestHandleListaPaises]:
        suite.addTests(loader.loadTestsFromTestCase(tc))

    out = os.path.join(os.path.dirname(__file__), "resultado_testes_geo.txt")
    with open(out,"w",encoding="utf-8") as f:
        result = unittest.TextTestRunner(stream=f, verbosity=2).run(suite)

    total  = result.testsRun
    falhas = len(result.failures) + len(result.errors)
    passou = total - falhas
    cob    = round((passou/total)*100,1) if total else 0

    with open(out,"a",encoding="utf-8") as f:
        f.write(f"\n{'='*55}\n  GEO Explorer — Resultado dos Testes\n{'='*55}\n")
        f.write(f"  Total    : {total}\n  ✅ Passou : {passou}\n  ❌ Falhou : {falhas}\n")
        f.write(f"  Cobertura: {cob}%  |  Meta: 70%\n")
        f.write(f"  {'✅ META ATINGIDA!' if cob>=70 else '❌ Meta não atingida'}\n{'='*55}\n")

    print(f"✅ Testes: {passou}/{total} | Cobertura: {cob}% | Log: {out}")
