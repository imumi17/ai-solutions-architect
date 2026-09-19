---
date: 2026-09-19
title: D4 - 2026-09-19 — Linux Processes
topic: Linux Processes
notion_page_id: 3e04fece-88b3-81ff-8187-cbb71fddcd6e
notion_page_url: https://app.notion.com/p/3e04fece88b381ff8187cbb71fddcd6e
---

# D4 - 2026-09-19 — Linux Processes

**Date:** September 19, 2026  
**Topic:** Linux Processes

**Goal:** Understand how Linux creates, monitors, and controls running programs.

## What I learned

### Quick reference — keyword heavy

| Command | Purpose | Remember |
|---------|---------|----------|
| `ps` | Process snapshot | Show currently running processes |
| `top` | Real-time monitoring | Live view of CPU, memory, load |
| `kill` | Send signal | Control/stop a process by PID |
| `jobs` | Background jobs | List jobs started from current shell |
| `bg` | Resume in background | Continue a stopped job in background |
| `fg` | Bring to foreground | Move background/stopped job to terminal |

---

### 1. `ps` → Process snapshot

**Purpose:** Show currently running processes.

```bash
ps
ps aux
ps -ef
ps aux | grep python
```

**Keywords:** `PID` • `PPID` • `USER` • `CPU` • `MEM` • `COMMAND`

| Term | Meaning |
|------|---------|
| **PID** | Process ID |
| **PPID** | Parent Process ID |
| `ps aux` | Detailed process list |
| `ps -ef` | Full-format process list |

---

### 2. `top` → Real-time processes

**Purpose:** Live view of system and process resource usage.

```bash
top
```

**Keywords:** `CPU` • `MEMORY` • `LOAD AVERAGE` • `PID`

Useful keys inside `top`:

| Key | Action |
|-----|--------|
| `q` | Quit |
| `k` | Kill process |
| `P` | Sort by CPU |
| `M` | Sort by memory |

---

### 3. `kill` → Send signal to process

**Purpose:** Stop or control a process using its PID.

```bash
kill PID
kill -9 PID
```

Common signals:

| Signal | Number | Effect |
|--------|--------|--------|
| `SIGTERM` | 15 | Graceful termination |
| `SIGKILL` | 9 | Force kill |
| `SIGSTOP` | 19 | Pause process |
| `SIGCONT` | 18 | Resume process |

**Remember:** `kill` sends a **signal** — it doesn't always mean "terminate."

---

### 4. `jobs` → Background jobs

**Purpose:** Show jobs started from the current shell.

```bash
jobs
```

Example:

```bash
sleep 100 &
jobs
```

Output might show:

```text
[1]+  Running    sleep 100 &
```

**Keywords:** `job ID` • `%1` • `background`

---

### 5. `bg` → Resume in background

**Purpose:** Continue a stopped job in the background.

```bash
bg
bg %1
```

Typical flow:

```bash
Ctrl + Z    # suspend
bg          # continue in background
```

---

### 6. `fg` → Bring to foreground

**Purpose:** Bring a background or stopped job back to the terminal.

```bash
fg
fg %1
```

Typical flow:

```bash
sleep 100 &
fg %1
```

---

### 🔑 Quick revision

```text
ps       → snapshot of processes
top      → live process monitoring
kill     → send signal to process
jobs     → list shell jobs
bg       → resume job in background
fg       → bring job to foreground
```

### ⭐ Must remember

```text
PID  = Process ID
PPID = Parent Process ID

&       → start in background
Ctrl+Z  → suspend current process
bg      → continue in background
fg      → bring to foreground
kill    → send signal
```

### 🧠 Mental model

```text
Program
   ↓
Process
   ↓
PID
   ↓
ps / top → observe
   ↓
kill     → control
   ↓
jobs     → shell jobs
   ↓
bg / fg  → move between background ↔ foreground
```

## What I built

A keyword-heavy quick-revision guide for Linux process management — from observing running programs to controlling shell jobs in foreground and background.

## What I broke

Nothing — this was a revision-only session.

## Why it broke

N/A

## Architecture decision

Treat process management as a **lifecycle workflow**:

1. **Observe** → `ps`, `top`
2. **Identify** → PID, PPID, owner, resource usage
3. **Control** → `kill` (signals, not just termination)
4. **Orchestrate** → `&`, `jobs`, `bg`, `fg` for shell-managed work

This maps directly to debugging stuck services, runaway scripts, and long-running jobs on servers and containers.

## Interview question

> *"What's the difference between `kill PID` and `kill -9 PID`? How do you run a command in the background and bring it back to the foreground?"*

**Answer sketch:** `kill PID` sends SIGTERM (15) for graceful shutdown; `kill -9` sends SIGKILL for immediate force kill. Use `command &` to background, `jobs` to list, `fg %1` to foreground. `Ctrl+Z` suspends; `bg` resumes in background.

## One thing I still don't understand

When to use shell job control (`bg`/`fg`) vs `systemd`, `nohup`, or `screen`/`tmux` for long-running production processes.
