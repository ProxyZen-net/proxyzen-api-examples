// ProxyZen API example (Node.js 18+, no dependencies). Docs: https://proxyzen.net/en/api
const API = 'https://proxyzen.net/api/v1';
const KEY = process.env.PROXYZEN_KEY || 'pz_your_key_here';

async function call(method, path, body) {
  const res = await fetch(API + path, {
    method,
    headers: { Authorization: `Bearer ${KEY}`, Accept: 'application/json', ...(body ? { 'Content-Type': 'application/json' } : {}) },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json();
  if (!res.ok) throw new Error(`${res.status} ${data.error.code}: ${data.error.message}`);
  return data;
}

console.log('Balance:', await call('GET', '/balance'));
console.log('Prices DE IPv4:', (await call('GET', '/prices?country=DE&type=ipv4')).data);

// Buy 1 IPv4 in Germany for 30 days (spends money — uncomment when ready)
// const order = await call('POST', '/orders', { country: 'DE', type: 'ipv4', quantity: 1, days: 30 });
// order.proxies.forEach(p => console.log(`${p.host}:${p.http_port}:${p.login}:${p.password}`));

for (const p of (await call('GET', '/proxies?status=active')).data) {
  console.log('Active:', `${p.host}:${p.http_port}`, 'until', p.expires_at);
}

console.log('Traffic prices:', (await call('GET', '/traffic/products')).data);
// await call('POST', '/traffic/orders', { type: 'residential', gb: 1 });   // spends money
for (const plan of (await call('GET', '/traffic/plans')).data) {
  const user = `${plan.username}-country-US-session-ab12cd-time-10`;
  console.log(`${plan.type}: ${plan.remaining_gb} GB left`);
  console.log(`  socks5://${user}:${plan.password}@${plan.host}:${plan.socks5_port}`);
}
