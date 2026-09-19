---
date: 2026-09-19
title: D5 - 2026-09-19 — Linux Networking CLI
topic: Linux Networking CLI
notion_page_id: 3e04fece-88b3-81b4-bbb5-de35cb1b7132
notion_page_url: https://app.notion.com/p/3e04fece88b381b4bbb5de35cb1b7132
---

# D5 - 2026-09-19 — Linux Networking CLI

**Date:** September 19, 2026  
**Topic:** Linux Networking CLI

**Goal:** Understand how to test connectivity, resolve DNS, inspect network connections, and connect to remote Linux machines.

## What I learned

### Quick reference — keyword heavy

| Command | Purpose | Remember |
|---------|---------|----------|
| `curl` | HTTP/API requests | Communicate with web servers and APIs |
| `ping` | Test connectivity | Check reachability and latency |
| `nslookup` / `dig` | DNS lookup | Translate domain names ↔ IP addresses |
| `ss` | Network sockets | View listening ports and active connections |
| `ssh` | Remote login | Securely connect to another Linux machine |

---

### 1. `curl` → HTTP/API requests

**Purpose:** Communicate with web servers and APIs from the terminal.

```bash
curl https://example.com
curl -I https://example.com
curl -X GET https://api.example.com
curl -X POST -H "Content-Type: application/json" \
  -d '{"name":"Umesh"}' https://api.example.com
```

**Keywords:** `HTTP` • `API` • `GET` • `POST` • `headers` • `status code`

| Flag | What it does |
|------|--------------|
| `-I` | Headers only |
| `-v` | Verbose / debug |
| `-o file` | Save response to file |

---

### 2. `ping` → Test connectivity

**Purpose:** Check whether a host is reachable and measure network latency.

```bash
ping google.com
ping -c 4 google.com
```

Example output:

```text
64 bytes from ...: time=12.3 ms
```

**Keywords:** `ICMP` • `latency` • `packet loss` • `reachability`

| Flag | What it does |
|------|--------------|
| `-c 4` | Send 4 packets |

> **Important:** A failed `ping` does **not necessarily mean the server is down**. ICMP may be blocked by a firewall.

---

### 3. `nslookup` / `dig` → DNS lookup

**Purpose:** Translate domain names ↔ IP addresses and inspect DNS records.

```bash
nslookup google.com
dig google.com
dig google.com A
dig google.com MX
dig google.com NS
```

**Keywords:** `DNS` • `domain` • `IP` • `A` • `MX` • `NS`

| Record | Meaning |
|--------|---------|
| `A` | IPv4 address |
| `AAAA` | IPv6 address |
| `CNAME` | Alias |
| `MX` | Mail server |
| `NS` | Name server |
| `TXT` | Text / verification records |

`dig` is generally preferred for **detailed DNS troubleshooting**.

---

### 4. `ss` → Network sockets / connections

**Purpose:** View listening ports and active network connections.

```bash
ss
ss -tuln
ss -tulpn
ss -tan
```

| Flag | Meaning |
|------|---------|
| `-t` | TCP |
| `-u` | UDP |
| `-l` | Listening |
| `-n` | Numeric addresses / ports |
| `-p` | Show process |
| `-a` | All |

Example:

```bash
ss -tuln
```

Could show:

```text
LISTEN  0  128  0.0.0.0:22
LISTEN  0  128  0.0.0.0:80
```

| Port | Service |
|------|---------|
| `22` | SSH |
| `80` | HTTP |

**Keywords:** `socket` • `port` • `LISTEN` • `TCP` • `UDP`

---

### 5. `ssh` → Remote login

**Purpose:** Securely connect to another Linux machine.

```bash
ssh user@server
```

Using an SSH key:

```bash
ssh -i my-key.pem user@server
```

Specify a port:

```bash
ssh -p 2222 user@server
```

Example:

```bash
ssh -i ec2-key.pem ec2-user@10.0.1.25
```

**Keywords:** `SSH` • `remote shell` • `authentication` • `key pair` • `port 22`

Basic flow:

```text
Your Machine
     │
     │ SSH
     ▼
Remote Linux Server
     │
     └── Terminal
```

---

### 🔑 Quick revision

```text
curl       → HTTP/API communication
ping       → connectivity + latency
nslookup   → DNS lookup
dig        → detailed DNS investigation
ss         → ports + network connections
ssh        → remote Linux access
```

### ⭐ Must remember

```text
curl URL              → request a website/API
curl -I URL           → response headers
ping host             → test reachability
dig domain            → DNS information
ss -tuln              → listening TCP/UDP ports
ssh user@host         → remote login
```

### 🧠 Networking mental model

```text
Domain
  │
  ▼
DNS          dig / nslookup
  │
  ▼
IP Address
  │
  ▼
Network Connectivity    ping
  │
  ▼
Port                    ss
  │
  ▼
Application             curl / ssh
```

**One-line interview memory:**

> **DNS finds the IP → `ping` tests reachability → `ss` checks ports → `curl` tests applications → `ssh` gives remote access.**

## What I built

A keyword-heavy quick-revision guide for Linux networking CLI — from DNS resolution through connectivity checks to port inspection and remote access.

## What I broke

Nothing — this was a revision-only session.

## Why it broke

N/A

## Architecture decision

Treat network debugging as a **layered diagnostic stack**:

1. **Name resolution** → `dig` / `nslookup`
2. **Reachability** → `ping`
3. **Port availability** → `ss -tuln`
4. **Application layer** → `curl`
5. **Remote access** → `ssh`

Work top-down: a failing `curl` might be DNS, firewall, closed port, or app error — each layer has its own tool.

## Interview question

> *"A service at `api.example.com` is unreachable. Walk me through how you'd debug it from the command line."*

**Answer sketch:** `dig api.example.com` (DNS resolves?) → `ping` (host reachable? note ICMP may be blocked) → `ss -tuln` on server (port listening?) → `curl -v https://api.example.com` (app responding?) → `ssh` into server for logs if needed.

## One thing I still don't understand

When to prefer `ss` over legacy `netstat`, and how container networking (Docker/K8s) changes what `ss` shows on the host vs inside a pod.
