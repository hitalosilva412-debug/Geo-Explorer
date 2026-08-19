"""
=============================================================
  GEO Explorer — MCP Service
  routes.py + server.py (unificado)
=============================================================
"""
import sys, os, json, argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from handlers import (handle_geo, handle_trilha_geo, handle_desafio_geo,
                      handle_certificado_geo, handle_lista_paises, handle_lista_tecnologias)


def _resp(data, status=200):
    body = json.dumps(data, ensure_ascii=False, indent=2)
    hdrs = {"Content-Type":"application/json; charset=utf-8",
            "Access-Control-Allow-Origin":"*",
            "X-Powered-By": f"{config.APP_NAME} v{config.VERSION}"}
    return status, hdrs, body

def _auth(headers):
    if config.AUTH_MODE == "none": return True
    key = headers.get("x-api-key","")
    return key in config.VALID_API_KEYS

def rotear(method, path, headers, body):
    p = urlparse(path)
    rota = p.path.rstrip("/")
    params = parse_qs(p.query)
    def q(k): return params.get(k,[None])[0]

    if rota in ("","/"): return _resp({"servico":config.APP_NAME,"versao":config.VERSION,"status":"online 🟢","docs":"/api/v1/docs"})
    if rota == "/api/v1/status": return _resp({"status":"online","versao":config.VERSION})
    if rota == "/api/v1/docs":
        return _resp({"endpoints":[
            {"method":"GET","path":"/","auth":False},
            {"method":"GET","path":"/api/v1/paises","auth":True},
            {"method":"GET","path":"/api/v1/tecnologias","auth":True},
            {"method":"GET","path":"/api/v1/geo?pais=X","auth":True},
            {"method":"GET","path":"/api/v1/trilha_geo?tech=X","auth":True},
            {"method":"GET","path":"/api/v1/desafio_geo?tech=X&nivel=Y","auth":True},
            {"method":"POST","path":"/api/v1/certificado_geo","auth":True},
            {"method":"POST","path":"/api/v1/auth/token","auth":False},
        ],"chaves_teste":["geo-dev-key-001","geo-dev-key-002"]})

    if rota == "/api/v1/auth/token" and method == "POST":
        data = json.loads(body or "{}")
        usuario = data.get("usuario","")
        if not usuario: return _resp({"erro":"'usuario' obrigatório"},400)
        import hmac, hashlib, base64, time
        h = lambda d: base64.urlsafe_b64encode(d).rstrip(b"=").decode()
        hdr = h(json.dumps({"alg":"HS256","typ":"JWT"}).encode())
        pld = h(json.dumps({"sub":usuario,"exp":int(time.time())+3600}).encode())
        sig = h(hmac.new(config.SSO_SECRET.encode(),f"{hdr}.{pld}".encode(),hashlib.sha256).digest())
        return _resp({"token":f"{hdr}.{pld}.{sig}","tipo":"Bearer","expira_em":"3600s"})

    if not _auth(headers):
        return _resp({"erro":"Não autenticado","dica":"Header X-API-Key obrigatório"},401)

    if rota == "/api/v1/paises" and method == "GET":
        r = handle_lista_paises(); return _resp(r, r["status"])
    if rota == "/api/v1/tecnologias" and method == "GET":
        r = handle_lista_tecnologias(); return _resp(r, r["status"])
    if rota == "/api/v1/geo" and method == "GET":
        r = handle_geo(q("pais") or ""); return _resp(r, r["status"])
    if rota == "/api/v1/trilha_geo" and method == "GET":
        r = handle_trilha_geo(q("tech") or ""); return _resp(r, r["status"])
    if rota == "/api/v1/desafio_geo" and method == "GET":
        r = handle_desafio_geo(q("tech") or "", q("nivel") or "Intermediário"); return _resp(r, r["status"])
    if rota == "/api/v1/certificado_geo" and method == "POST":
        data = json.loads(body or "{}")
        r = handle_certificado_geo(data.get("nome",""), data.get("tecnologia","")); return _resp(r, r["status"])

    return _resp({"erro":f"Rota '{rota}' não encontrada","docs":"/api/v1/docs"},404)


class GEOHandler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {self.address_string()} {fmt%args}")
    def _handle(self, method):
        length = int(self.headers.get("Content-Length",0))
        body = self.rfile.read(length).decode("utf-8") if length else ""
        hdrs = {k.lower():v for k,v in self.headers.items()}
        status, resp_hdrs, resp_body = rotear(method, self.path, hdrs, body)
        self.send_response(status)
        for k,v in resp_hdrs.items(): self.send_header(k,v)
        enc = resp_body.encode("utf-8")
        self.send_header("Content-Length", str(len(enc)))
        self.end_headers(); self.wfile.write(enc)
    def do_GET(self):    self._handle("GET")
    def do_POST(self):   self._handle("POST")
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers","Content-Type,X-API-Key,Authorization")
        self.end_headers()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=config.PORT)
    parser.add_argument("--auth", choices=["none","apikey","sso"], default=config.AUTH_MODE)
    args = parser.parse_args()
    config.PORT = args.port; config.AUTH_MODE = args.auth
    print(f"""
╔══════════════════════════════════════════════╗
║     🌍 GEO Explorer MCP Service v1.0.0       ║
╠══════════════════════════════════════════════╣
║  GET  /api/v1/paises                         ║
║  GET  /api/v1/tecnologias                    ║
║  GET  /api/v1/geo?pais=X                     ║
║  GET  /api/v1/trilha_geo?tech=X              ║
║  GET  /api/v1/desafio_geo?tech=X&nivel=Y     ║
║  POST /api/v1/certificado_geo                ║
║  POST /api/v1/auth/token                     ║
╚══════════════════════════════════════════════╝
  🌐 http://localhost:{args.port}  |  Auth: {args.auth}
""")
    srv = HTTPServer((config.HOST, args.port), GEOHandler)
    try: srv.serve_forever()
    except KeyboardInterrupt: print("\n⛔ Servidor encerrado."); srv.server_close()

if __name__ == "__main__": main()
