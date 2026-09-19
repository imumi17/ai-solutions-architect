---
date: 2026-09-16
title: D1 - 2026-09-16 — Linux Filesystem Quick Revision
topic: Linux Filesystem — Quick Revision Notes
notion_page_id: 3dd4fece-88b3-8196-957c-fd133609edcb
notion_page_url: https://app.notion.com/p/3dd4fece88b38196957cfd133609edcb
---

# D1 - 2026-09-16 — Linux Filesystem Quick Revision

**Date:** September 16, 2026  
**Topic:** Linux Filesystem — Quick Revision Notes

## What I learned

Linux uses a **single unified directory tree** starting at `/` (root). Every path is absolute from root or relative from the current working directory.

| Path | Purpose | What lives here | Examples |
|------|---------|-----------------|----------|
| `/` | **ROOT** — top of the entire filesystem | Everything starts here | Foundation of all paths |
| `/home` | **USERS** — personal files | Per-user home directories | `/home/ubuntu`, `/home/user`, `~` |
| `/etc` | **CONFIG** — system & app settings | Static configuration files | `/etc/hosts`, `/etc/passwd`, `/etc/fstab`, `/etc/ssh/` |
| `/var` | **VARIABLE DATA** — changing runtime data | Logs, caches, app state | `/var/log`, `/var/lib`, `/var/cache` |
| `/tmp` | **TEMPORARY** — short-lived files | Ephemeral scratch space | May be cleaned on reboot — don't store permanent data |

### `/var` breakdown

- **`/var/log`** → system & application **logs**
- **`/var/lib`** → application **state** and persistent runtime data
- **`/var/cache`** → **cache** files (safe to clear in many cases)

### Relative path shortcuts

- `.` → **current directory**
- `..` → **parent directory**

### Memory trick

| Symbol | Mnemonic |
|--------|----------|
| `/` | Everything |
| `/home` | Humans 👤 |
| `/etc` | Settings ⚙️ |
| `/var` | Variable / changing data 🔄 |
| `/tmp` | Temporary 🗑️ |

### Interview keywords

| Path | Keywords |
|------|----------|
| `/` | Root, filesystem, top-level |
| `/home` | Users, personal files, `~` |
| `/etc` | Configuration, system settings |
| `/var` | Logs, cache, application state |
| `/tmp` | Temporary, ephemeral, cleanup |

**One-liner:** Linux is one tree starting at `/`; `/home` holds users, `/etc` config, `/var` changing data, `/tmp` temporary data.

## What I built

A quick-revision cheat sheet for the core Linux directory hierarchy — structured for interview prep and day-to-day navigation on servers and cloud VMs.

## What broke

Nothing — this was a revision-only session.

## Why it broke

N/A

## Architecture decision

Treat the Linux filesystem as a **hierarchy of concerns**, not random folders:

- **Immutable-ish config** → `/etc`
- **User-owned workspace** → `/home`
- **Mutable runtime state** → `/var`
- **Ephemeral scratch** → `/tmp`

When designing deployments or debugging production issues, knowing *which layer* a path belongs to tells you whether data should persist, be backed up, or is safe to wipe.

## Interview question

> *"Explain the purpose of `/etc`, `/var`, and `/tmp`. Where would you look for application logs, and why shouldn't you store important data in `/tmp`?"*

**Answer sketch:** `/etc` holds configuration; `/var` holds variable runtime data including logs under `/var/log`; `/tmp` is ephemeral and may be cleared on reboot or by cleanup jobs — so critical data there risks loss.

## One thing I still don't understand

How distributions differ in what they place under `/opt` vs `/usr/local` vs `/var/lib` for third-party applications — and when that distinction matters in containerized vs bare-metal deployments.
