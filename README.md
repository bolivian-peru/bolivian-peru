<img src="assets/header.gif" width="100%" alt="bolivian-peru — builds rails for ai agents: proxies, servers, payments">

hi. i'm peruvian.

i point fleets of agents at the boring, load-bearing parts that ai agents need to do real work on the real internet: an ip address that looks like a person on a phone, a server they can run without ssh, and a way to pay for both without a credit card or a sales call.

most of it started as an afternoon with claude code and a strong opinion. some of it turned into companies.

<img src="assets/now.gif" width="100%" alt="~/now">

```text
role        master ai-agent controller. agents write the code, i decide what ships
working on  proxies agents can rent by the gigabyte · an os you talk to · ai for old-school companies
stack       all of it. whatever the job needs, the agents write it; rust to kotlin, nix to solana
believes    if a number can't be traced to a source, it doesn't ship
```

<img src="assets/shipped.gif" width="100%" alt="~/shipped">

**[proxies.sx](https://proxies.sx)**: a pool gateway for mobile and residential proxies. one endpoint, and the proxy username decides the country, pool and session. metered per gb; agents can pay in usdc over [x402](https://www.x402.org) with no account at all ([agents.proxies.sx](https://agents.proxies.sx)).

**[coronium.io](https://coronium.io)**: dedicated 4g/5g mobile proxies on real carrier sims. the agent-facing side lives in [`coronium-ai`](https://github.com/bolivian-peru/coronium-ai) (typed sdk + cli) and [`coronium-reseller-kit`](https://github.com/bolivian-peru/coronium-reseller-kit).

**[osmoda](https://github.com/bolivian-peru/os-moda)**: an operating system for ai agents, built on nixos. you talk to your server instead of ssh-ing into it, and every change is a transaction you can roll back. 10 rust daemons, 92 typed tools, honest about being research-grade.

**[northwestern solutions](https://northwesternsolutions.org)**: ai for lithuanian manufacturers, wholesalers and logistics firms: the companies that quietly keep the country running, often on excel. plus an app builder that turns their spreadsheets into working tools.

<img src="assets/oss.gif" width="100%" alt="~/open-source">

| repo | what it does |
|---|---|
| [`os-moda`](https://github.com/bolivian-peru/os-moda) | the agent os above. rust, nixos, mcp, atomic rollback |
| [`proxies-sx-mcp-server`](https://github.com/bolivian-peru/proxies-sx-mcp-server) | 70 mcp tools so claude / cursor can buy, rotate and route proxies. `npx -y @proxies-sx/mcp-server` |
| [`proxy-reseller-kit`](https://github.com/bolivian-peru/proxy-reseller-kit) | sdk, drop-in react component and next.js storefront: run a branded proxy business in an afternoon |
| [`marketplace-service-template`](https://github.com/bolivian-peru/marketplace-service-template) | fork, edit one file, deploy: sell an api to agents, get paid in usdc |
| [`android-peer-sdk`](https://github.com/bolivian-peru/android-peer-sdk) | share a phone's spare bandwidth, earn usdc. three lines via jitpack |
| [`x402-sdk`](https://github.com/bolivian-peru/x402-sdk) | x402 micropayments on base and solana, as hono middleware |
| [`browser-proxies-sx`](https://github.com/bolivian-peru/browser-proxies-sx) | cloud antidetect browser with identity bundles and an auto-assigned mobile ip |
| [`baozi-mcp`](https://github.com/bolivian-peru/baozi-mcp) | 68 tools for agents trading [baozi.bet](https://baozi.bet) prediction markets on solana |
| [`bolivian-peru-ai-skills`](https://github.com/bolivian-peru/bolivian-peru-ai-skills) | agent skills that read your real code: live 3d system maps, plantuml, no mock data |

<img src="assets/side.gif" width="100%" alt="~/side-quests">

- **[`vilnius-3d-game`](https://github.com/bolivian-peru/vilnius-3d-game)**: the real city of vilnius at 1:1 in the browser. streamed photomesh, every osm street drivable, a car with actual tyre physics. heading somewhere vice-city-shaped.
- **[wizarscape](https://game.wizardwifhat.com)** (beta): an old-school wizard mmo that runs in thy browser, phone included. six elemental classes, duels, rune crafting, rare drops, gear to +10. no download.
- **[fermos.lt](https://fermos.lt)**: a registry of lithuanian farms, matched to the eu subsidy calls they can actually apply for.
- **[`openclaw-oauth-runtime-restore`](https://github.com/bolivian-peru/openclaw-oauth-runtime-restore)**: proof that your software moat is someone's afternoon claude code session.

<img src="assets/contact.gif" width="100%" alt="~/say-hi">

open an issue on any repo, or find me through [proxies.sx](https://proxies.sx), [coronium.io](https://coronium.io) or [os.moda](https://os.moda). happy to talk agents, proxies, nix, or why a lowercase readme is a personality.

<img src="assets/footer.gif" width="100%" alt="">
