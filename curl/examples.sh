#!/usr/bin/env bash
# ProxyZen API with curl. Docs: https://proxyzen.net/en/api
KEY="${PROXYZEN_KEY:-pz_your_key_here}"
API=https://proxyzen.net/api/v1

curl -s "$API/balance" -H "Authorization: Bearer $KEY"
curl -s "$API/countries" -H "Authorization: Bearer $KEY"
curl -s "$API/prices?country=DE&type=ipv4" -H "Authorization: Bearer $KEY"

# Buy 2 IPv4 proxies in Germany for 30 days
# curl -s -X POST "$API/orders" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
#   -d '{"country":"DE","type":"ipv4","quantity":2,"days":30}'

curl -s "$API/proxies?status=active&per_page=500" -H "Authorization: Bearer $KEY"

# Renew proxies (same IPs) for 30 days
# curl -s -X POST "$API/proxies/renew" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" -d '{"ids":[5001,5002],"days":30}'

# Residential / mobile traffic
curl -s "$API/traffic/products" -H "Authorization: Bearer $KEY"
# curl -s -X POST "$API/traffic/orders" -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" -d '{"type":"residential","gb":5}'
curl -s "$API/traffic/plans" -H "Authorization: Bearer $KEY"
