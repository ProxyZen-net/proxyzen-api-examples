<?php
// ProxyZen API example (PHP 8 + curl). Docs: https://proxyzen.net/en/api

const API = 'https://proxyzen.net/api/v1';
$key = getenv('PROXYZEN_KEY') ?: 'pz_your_key_here';

function call(string $method, string $path, ?array $body = null): array
{
    global $key;
    $ch = curl_init(API.$path);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST => $method,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => 60,
        CURLOPT_HTTPHEADER => ["Authorization: Bearer $key", 'Accept: application/json', 'Content-Type: application/json'],
        CURLOPT_POSTFIELDS => $body ? json_encode($body) : null,
    ]);
    $data = json_decode(curl_exec($ch), true);
    $status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($status >= 400) {
        throw new RuntimeException("$status {$data['error']['code']}: {$data['error']['message']}");
    }

    return $data;
}

print_r(call('GET', '/balance'));
print_r(call('GET', '/prices?country=DE&type=ipv4')['data']);

// Buy 1 IPv4 in Germany for 30 days (spends money — uncomment when ready)
// $order = call('POST', '/orders', ['country' => 'DE', 'type' => 'ipv4', 'quantity' => 1, 'days' => 30]);
// foreach ($order['proxies'] as $p) echo "{$p['host']}:{$p['http_port']}:{$p['login']}:{$p['password']}\n";

foreach (call('GET', '/proxies?status=active')['data'] as $p) {
    echo "Active: {$p['host']}:{$p['http_port']} until {$p['expires_at']}\n";
}

foreach (call('GET', '/traffic/plans')['data'] as $plan) {
    $user = "{$plan['username']}-country-DE";
    echo "{$plan['type']}: {$plan['remaining_gb']} GB left — http://$user:{$plan['password']}@{$plan['host']}:{$plan['http_port']}\n";
}
