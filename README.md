# V2Ray Docker Compose

This repository introduces V2Ray-based solutions to bypass limitations in highly restricted networks
without direct/safe/stable access to upstream servers (servers with access to free Internet).

this project fork from [miladrahimi/v2ray-docker-compose](https://github.com/miladrahimi/v2ray-docker-compose)
and keep only v2ray + Caddy config for self used.


## Table of contents

  * [Server Solutions](#server-solutions)
    * [V2Ray Behind a CDN Service](#v2ray-behind-a-cdn-service)
  * [Client Applications](#client-applications)
    * [VMESS Protocol](#vmess-protocol)
    * [Shadowsocks Protocol](#shadowsocks-protocol)
    * [HTTP and SOCKS Protocols](#http-and-socks-protocols)
  * [Subscription Link](#subscription-link)
  * [Tips](#tips)
  * [Docker Images](#docker-images)
  * [More](#more)
  * [Star History](#star-history)

## Server Solutions

### V2Ray Behind a CDN Service

In this solution, you need one server (upstream) and a domain/subdomain added to a CDN service.

* Upstream Server: A server that has free access to the Internet.
* CDN Service: A Content delivery network like [Cloudflare](//cloudflare.com), [ArvanCloud](//arvancloud.ir) or [DerakCloud](//derak.cloud).

```
(Client) <-> [ CDN Service ] <-> [ Upstream Server ] <-> (Internet)
```

This solution provides VMESS over Websockets + TLS + CDN.
[Read more...](https://guide.v2fly.org/en_US/advanced/wss_and_web.html)

Follow these steps to setup V2Ray + Caddy (Web server) + CDN:

1. In your CDN, create an `A` record pointing to your server IP with the proxy option turned off.
1. Install Docker and Docker-compose on your server.
1. Copy the whole project code into the server.1.

1. run `python3 ./setup.py` to generate config files
1. Run `docker-compose up -d`.
1. Visit your domain/subdomain in your web browser.
   Wait until the [homepage](caddy/web/index.html) is loaded.
1. (Optional) In your CDN, turn the proxy option on for the record.
1. Run `./vmess.py` to generate client configuration (link).

Some CDN services don't offer unlimited traffic for free plans.
Please check [CDN Free Plans](https://github.com/miladrahimi/v2ray-docker-compose/discussions/89).

You don't need to turn the cloud (proxy) on in your CDN (step 10) when the Internet is not blocked.
When it's off, clients connect to the server directly and CDN services also don't charge you any fee.

## Client Applications

### VMESS Protocol

This is the list of recommended applications to use the VMESS protocol:

* [Nekoray](https://github.com/MatsuriDayo/nekoray/releases) for macOS, Windows, and Linux
* [Qv2ray](https://qv2ray.net) for macOS, Windows, and Linux
* [V2RayX](https://github.com/Cenmrev/V2RayX/releases) for macOS
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS
* [v2rayNG](https://github.com/2dust/v2rayNG) for Android

### Shadowsocks Protocol

This is the list of recommended applications to use the Shadowsocks protocol:

* [Outline](https://getoutline.org/get-started/#step-3) for all platforms
* [ShadowsocksX-NG](https://github.com/shadowsocks/ShadowsocksX-NG/releases) for macOS
* [shadowsocks-libev](https://github.com/shadowsocks/shadowsocks-libev) for Linux
* [shadowsocks-windows](https://github.com/shadowsocks/shadowsocks-windows/releases)
* [shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases)
* [ShadowLink](https://apps.apple.com/us/app/shadowlink-shadowsocks-vpn/id1439686518) for iOS

## Tips

* Some hostings might ban your proxy traffic. Use an appropriate hosting.
* Some Internet providers might ban your proxy traffic. Changing AlterID could be helpful.
  See [#57](https://github.com/miladrahimi/v2ray-docker-compose/issues/57).

## Docker Images

By default, this repository uses the GitHub registry.
You can modify the Docker-compose file to use Docker Hub.

* GitHub:
  * Image: ```ghcr.io/getimages/v2fly-core:v4.45.2```
  * URL: https://github.com/orgs/getimages/packages/container/package/v2fly-core
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`
* Docker Hub:
  * Image: ```v2fly/v2fly-core:v4.45.2```
  * URL: https://hub.docker.com/r/v2fly/v2fly-core/tags
  * Digest: `sha256:289fc9451f21a265f95615e29f05ea23bc32026db152863eee317738813521d7`

## More
* [V2Ray Config Examples](https://github.com/xesina/v2ray-config-examples)
* [NekoRay Installer (for Linux)](https://github.com/ohmydevops/nekoray-installer)
* [V2Ray Ansible](https://github.com/ohmydevops/v2ray-ansible)
* [V2Fly (V2Ray)](https://www.v2fly.org)
* [V2Fly (V2Ray) configurations](https://guide.v2fly.org)
