"""ProxyZen API example (Python 3 + requests). Docs: https://proxyzen.net/en/api"""
import os

import requests

API = "https://proxyzen.net/api/v1"
KEY = os.environ.get("PROXYZEN_KEY", "pz_your_key_here")
s = requests.Session()
s.headers.update({"Authorization": f"Bearer {KEY}", "Accept": "application/json"})


def call(method: str, path: str, **kw):
    r = s.request(method, API + path, timeout=60, **kw)
    data = r.json()
    if r.status_code >= 400:
        raise RuntimeError(f"{r.status_code} {data['error']['code']}: {data['error']['message']}")
    return data


print("Balance:", call("GET", "/balance"))

# IPv4 / IPv6: countries in stock and prices
countries = call("GET", "/countries")["data"]
in_stock = [c for c in countries if c["available"]["ipv4"] > 0]
print("IPv4 countries in stock:", ", ".join(c["code"] for c in in_stock[:15]))
print("Prices DE IPv4:", call("GET", "/prices", params={"country": "DE", "type": "ipv4"})["data"])

# Buy 1 IPv4 in Germany for 30 days (spends money — uncomment when ready)
# order = call("POST", "/orders", json={"country": "DE", "type": "ipv4", "quantity": 1, "days": 30})
# for p in order["proxies"]:
#     print(f"{p['host']}:{p['http_port']}:{p['login']}:{p['password']}")

for p in call("GET", "/proxies", params={"status": "active"})["data"]:
    print("Active:", f"{p['host']}:{p['http_port']}", "until", p["expires_at"])

# Residential / mobile traffic (per GB)
print("Traffic prices:", call("GET", "/traffic/products")["data"])
# call("POST", "/traffic/orders", json={"type": "residential", "gb": 1})   # spends money
for plan in call("GET", "/traffic/plans")["data"]:
    user = f"{plan['username']}-country-US-session-ab12cd-time-10"     # US, one IP for 10 minutes
    print(f"{plan['type']}: {plan['remaining_gb']} GB left")
    print(f"  http://{user}:{plan['password']}@{plan['host']}:{plan['http_port']}")
