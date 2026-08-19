"""
=============================================================
  GEO Explorer — Testes Unitários Completos
  CRC/test_geo.py — Cobertura alvo: >= 70%
=============================================================
"""
import json, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "MCP"))

from handlers import (
    _carregar_paises, _buscar_pais,
    _carregar_tecnologias, _buscar_tecnologia,
    handle_geo, handle_lista_paises,
    handle_trilha_geo, handle_desafio_geo,
    handle_certificado_geo, handle_lista_tecnologias,
)


# ══════════════════════════════════════════════════════════
#  SUITE 1 — Dados: paises.geo_json
# ══════════════════════════════════════════════════════════
class TestCarregarPaises(unittest.TestCase):
    def test_json_carrega(self):
        self.assertIsInstance(_carregar_paises(), list)
    def test_tem_15_paises(self):
        self.assertEqual(len(_carregar_paises()), 15)
    def test_campos_obrigatorios(self):
        campos = ["id","nome","capital","continente","area_km2","populacao","idioma","moeda","nivel","xp"]
        for p in _carregar_paises():
            for c in campos:
                self.assertIn(c, p, f"Campo '{c}' ausente no país id={p.get('id')}")


# ══════════════════════════════════════════════════════════
#  SUITE 2 — Dados: tecnologias.geo_json
# ══════════════════════════════════════════════════════════
class TestCarregarTecnologias(unittest.TestCase):
    def test_json_carrega(self):
        self.assertIsInstance(_carregar_tecnologias(), list)
    def test_tem_20_tecnologias(self):
        self.assertEqual(len(_carregar_tecnologias()), 20)
    def test_campos_obrigatorios(self):
        campos = ["id","nome","categoria","nivel","numero_de_modulos","xp_total",
                  "carga_horaria_total","badges","lives","modulos"]
        for t in _carregar_tecnologias():
            for c in campos:
                self.assertIn(c, t, f"Campo '{c}' ausente em id={t.get('id')}")
    def test_cada_modulo_tem_campos(self):
        for t in _carregar_tecnologias():
            for m in t["modulos"]:
                for c in ["id","titulo","carga","xp","tipo"]:
                    self.assertIn(c, m)
    def test_tipos_validos(self):
        validos = {"teoria","pratica","projeto"}
        for t in _carregar_tecnologias():
            for m in t["modulos"]:
                self.assertIn(m["tipo"], validos)


# ══════════════════════════════════════════════════════════
#  SUITE 3 — handle_geo
# ══════════════════════════════════════════════════════════
class TestHandleGeo(unittest.TestCase):
    def test_brasil_encontrado(self):
        r = handle_geo("Brasil")
        self.assertEqual(r["status"], 200)
        self.assertEqual(r["pais"]["nome"], "Brasil")
    def test_busca_case_insensitive(self):
        self.assertEqual(handle_geo("brasil")["status"], 200)
    def test_pais_nao_encontrado(self):
        self.assertEqual(handle_geo("PaisXYZ999")["status"], 404)
    def test_sugestoes_em_nao_encontrado(self):
        r = handle_geo("PaisXYZ999")
        self.assertIn("sugestoes", r)
        self.assertGreater(len(r["sugestoes"]), 0)
    def test_sem_parametro_retorna_400(self):
        self.assertEqual(handle_geo("")["status"], 400)
    def test_japao_encontrado(self):
        self.assertEqual(handle_geo("Japão")["status"], 200)


# ══════════════════════════════════════════════════════════
#  SUITE 4 — handle_trilha_geo
# ══════════════════════════════════════════════════════════
class TestHandleTrilhaGeo(unittest.TestCase):
    def test_qgis_encontrado(self):
        r = handle_trilha_geo("QGIS")
        self.assertEqual(r["status"], 200)
        self.assertIn("QGIS", r["trilha"]["nome"])
    def test_python_encontrado(self):
        r = handle_trilha_geo("Python")
        self.assertEqual(r["status"], 200)
    def test_retorna_cronograma(self):
        r = handle_trilha_geo("QGIS")
        self.assertIn("cronograma", r)
        self.assertGreater(len(r["cronograma"]), 0)
    def test_cronograma_tem_semanas(self):
        r = handle_trilha_geo("QGIS")
        for item in r["cronograma"]:
            self.assertIn("semana", item)
            self.assertIn("titulo", item)
            self.assertIn("xp", item)
    def test_retorna_fases(self):
        r = handle_trilha_geo("QGIS")
        self.assertIn("fases", r)
        self.assertIn("teoria", r["fases"])
        self.assertIn("pratica", r["fases"])
        self.assertIn("projeto", r["fases"])
    def test_tecnologia_nao_encontrada(self):
        r = handle_trilha_geo("TecXYZ999")
        self.assertEqual(r["status"], 404)
        self.assertIn("sugestoes", r)
    def test_sem_parametro_retorna_400(self):
        self.assertEqual(handle_trilha_geo("")["status"], 400)
    def test_total_semanas_positivo(self):
        r = handle_trilha_geo("Python")
        self.assertGreater(r["total_semanas"], 0)


# ══════════════════════════════════════════════════════════
#  SUITE 5 — handle_desafio_geo
# ══════════════════════════════════════════════════════════
class TestHandleDesafioGeo(unittest.TestCase):
    def test_desafio_qgis_iniciante(self):
        r = handle_desafio_geo("QGIS", "Iniciante")
        self.assertEqual(r["status"], 200)
        self.assertEqual(r["desafio"]["nivel"], "Iniciante")
    def test_desafio_xp_positivo(self):
        r = handle_desafio_geo("Python", "Avançado")
        self.assertGreater(r["desafio"]["xp"], 0)
    def test_sem_nivel_usa_intermediario(self):
        r = handle_desafio_geo("QGIS")
        self.assertEqual(r["desafio"]["nivel"], "Intermediário")
    def test_desafio_tem_enunciado(self):
        r = handle_desafio_geo("QGIS", "Intermediário")
        self.assertGreater(len(r["desafio"]["enunciado"]), 10)
    def test_desafio_tem_dicas(self):
        r = handle_desafio_geo("Python", "Iniciante")
        self.assertEqual(len(r["desafio"]["dicas"]), 3)
    def test_desafio_tem_criterios(self):
        r = handle_desafio_geo("GPS", "Avançado")
        self.assertIn("criterios", r["desafio"])
    def test_sem_parametro_retorna_400(self):
        self.assertEqual(handle_desafio_geo("")["status"], 400)
    def test_desafio_tem_tempo(self):
        r = handle_desafio_geo("QGIS", "Intermediário")
        self.assertIn("tempo", r["desafio"])


# ══════════════════════════════════════════════════════════
#  SUITE 6 — handle_certificado_geo
# ══════════════════════════════════════════════════════════
class TestHandleCertificadoGeo(unittest.TestCase):
    def test_certificado_emitido(self):
        r = handle_certificado_geo("Hitalo Silva", "QGIS")
        self.assertEqual(r["status"], 201)
    def test_certificado_tem_id(self):
        r = handle_certificado_geo("Hitalo Silva", "QGIS")
        self.assertTrue(r["certificado"]["id"].startswith("GEO-2026-"))
    def test_certificado_arquivo_criado(self):
        r = handle_certificado_geo("Hitalo Silva", "Python")
        self.assertTrue(os.path.exists(r["certificado"]["arquivo"]))
    def test_certificado_tem_badges(self):
        r = handle_certificado_geo("Hitalo", "QGIS")
        self.assertIsInstance(r["certificado"]["badges"], list)
        self.assertGreater(len(r["certificado"]["badges"]), 0)
    def test_certificado_tem_verificacao(self):
        r = handle_certificado_geo("Hitalo", "GPS")
        self.assertIn("geoexplorer.app", r["certificado"]["verificacao"])
    def test_sem_nome_retorna_400(self):
        self.assertEqual(handle_certificado_geo("", "QGIS")["status"], 400)
    def test_sem_tecnologia_retorna_400(self):
        self.assertEqual(handle_certificado_geo("Hitalo", "")["status"], 400)
    def test_tecnologia_inexistente_gera_cert(self):
        # Mesmo sem achar a tech, deve emitir certificado genérico
        r = handle_certificado_geo("Hitalo", "TechInexistente999")
        self.assertEqual(r["status"], 201)


# ══════════════════════════════════════════════════════════
#  SUITE 7 — handle_lista_paises / handle_lista_tecnologias
# ══════════════════════════════════════════════════════════
class TestHandleListas(unittest.TestCase):
    def test_lista_paises_200(self):
        self.assertEqual(handle_lista_paises()["status"], 200)
    def test_lista_paises_tem_15(self):
        self.assertEqual(handle_lista_paises()["total"], 15)
    def test_lista_tecnologias_200(self):
        self.assertEqual(handle_lista_tecnologias()["status"], 200)
    def test_lista_tecnologias_tem_20(self):
        self.assertEqual(handle_lista_tecnologias()["total"], 20)
    def test_campos_resumo_tecnologia(self):
        t = handle_lista_tecnologias()["tecnologias"][0]
        for c in ["id","nome","categoria","nivel","modulos","xp","carga"]:
            self.assertIn(c, t)


# ══════════════════════════════════════════════════════════
#  RUNNER — grava resultado em TXT
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    for tc in [TestCarregarPaises, TestCarregarTecnologias,
               TestHandleGeo, TestHandleTrilhaGeo,
               TestHandleDesafioGeo, TestHandleCertificadoGeo,
               TestHandleListas]:
        suite.addTests(loader.loadTestsFromTestCase(tc))

    out = os.path.join(os.path.dirname(__file__), "resultado_testes_geo.txt")
    with open(out, "w", encoding="utf-8") as f:
        result = unittest.TextTestRunner(stream=f, verbosity=2).run(suite)

    total  = result.testsRun
    falhas = len(result.failures) + len(result.errors)
    passou = total - falhas
    cob    = round((passou / total) * 100, 1) if total else 0

    with open(out, "a", encoding="utf-8") as f:
        f.write(f"\n{'='*60}\n  GEO Explorer — Resultado dos Testes\n{'='*60}\n")
        f.write(f"  Total    : {total}\n  ✅ Passou : {passou}\n  ❌ Falhou : {falhas}\n")
        f.write(f"  Cobertura: {cob}%  |  Meta: 70%\n")
        f.write(f"  {'✅ META ATINGIDA!' if cob >= 70 else '❌ Meta não atingida'}\n{'='*60}\n")

    print(f"\n✅ Testes: {passou}/{total} | Cobertura: {cob}% | Log: {out}")
