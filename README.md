# ProxyZen API examples

Ready-to-run examples for the [ProxyZen](https://proxyzen.net) proxy API: check your balance, buy IPv4/IPv6 proxies, list and renew them, buy residential or mobile traffic and build a connection string.

- 📖 Full documentation: https://proxyzen.net/en/api
- 🔑 Get an API key: [dashboard → API](https://proxyzen.net/cabinet/api)
- Base URL: `https://proxyzen.net/api/v1` · auth header: `Authorization: Bearer pz_…`

| Language | File | Run |
|---|---|---|
| Python 3 | [`python/proxyzen.py`](python/proxyzen.py) | `pip install requests && PROXYZEN_KEY=pz_… python proxyzen.py` |
| Node.js 18+ | [`nodejs/proxyzen.mjs`](nodejs/proxyzen.mjs) | `PROXYZEN_KEY=pz_… node proxyzen.mjs` |
| PHP 8 | [`php/proxyzen.php`](php/proxyzen.php) | `PROXYZEN_KEY=pz_… php proxyzen.php` |
| curl | [`curl/examples.sh`](curl/examples.sh) | copy any command |

The examples only **read** data by default. Lines that spend money (buying proxies or traffic) are commented out — uncomment them when you are ready.

## Main endpoints

| Method | Path | What it does |
|---|---|---|
| GET | `/balance` | Your balance and personal discount |
| GET | `/countries` | Countries and how many IPs are in stock |
| GET | `/prices?country=DE&type=ipv4` | Prices per IP for every period |
| POST | `/orders` | Buy IPv4/IPv6 proxies (`country`, `type`, `quantity`, `days`) |
| GET | `/proxies` | Your proxies (`status`, `per_page`, `page`) |
| POST | `/proxies/renew` | Renew the same IPs (`ids`, `days`) |
| GET | `/traffic/products` | Residential and mobile prices per GB, host and ports |
| POST | `/traffic/orders` | Buy GB of residential or mobile traffic (`type`, `gb`) |
| GET | `/traffic/plans` | Your traffic plans: username, password, GB left |

**Targeting residential and mobile proxies:** add options to the username — `USERNAME-country-DE`, `-state-<code>`, `-city-<code>`, `-asn-<code>`, and `-session-ab12cd-time-10` for one IP for 10 minutes. Codes come from `GET /traffic/countries/DE?type=residential`.

## Resell under your own brand
Want a Telegram shop instead of writing code? Use the free [ProxyZen Telegram Shop](https://github.com/proxyzen/proxyzen-telegram-shop) script — install it in 5 minutes and set your own prices.

---

Questions: [@proxyzen_agent](https://t.me/proxyzen_agent) · https://proxyzen.net
