"""
=============================================================
  GEO Explorer — MCP Service
  config.py
=============================================================
"""
import os

HOST         = os.getenv("GEO_HOST", "0.0.0.0")
PORT         = int(os.getenv("GEO_PORT", 8090))
DEBUG        = os.getenv("GEO_DEBUG", "true").lower() == "true"
APP_NAME     = "GEO Explorer MCP Service"
VERSION      = "1.0.0"
AUTH_MODE    = os.getenv("GEO_AUTH_MODE", "apikey")
VALID_API_KEYS = set(os.getenv("GEO_API_KEYS", "geo-dev-key-001,geo-dev-key-002").split(","))
SSO_SECRET   = os.getenv("GEO_SSO_SECRET", "geo-sso-secret-2026")
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
DATA_DIR     = os.path.join(BASE_DIR, "..", "DATA")
CERTS_DIR    = os.path.join(BASE_DIR, "..", "docs", "certificados-emitidos")
PAISES_JSON  = os.path.join(DATA_DIR, "paises.geo_json")
