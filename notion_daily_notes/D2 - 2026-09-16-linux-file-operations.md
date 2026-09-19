---
date: 2026-09-16
title: D2 - 2026-09-16 — Linux File Operations
topic: Linux File Operations
notion_page_id: 3dd4fece-88b3-81a0-b726-ca3581134f6d
notion_page_url: https://app.notion.com/p/3dd4fece88b381a0b726ca3581134f6d
---

# D2 - 2026-09-16 — Linux File Operations

**Date:** September 16, 2026  
**Topic:** Linux File Operations

## What I learned

### Quick reference — keyword heavy

| Command | Meaning | Key usage |
|---------|---------|-----------|
| `ls` | **List** | View files and directories |
| `cd` | **Change Directory** | Move between directories |
| `pwd` | **Print Working Directory** | Show current location |
| `cp` | **Copy** | Copy files/directories |
| `mv` | **Move / Rename** | Move or rename |
| `rm` | **Remove** | Delete files/directories |
| `mkdir` | **Make Directory** | Create directory |
| `touch` | **Create / Update** | Create empty file or update timestamp |
| `find` | **Search** | Find files/directories by name, type, size, time, etc. |

---

### 1. `ls` → List

```bash
ls
```

**Think:** `LIST → what's here?`

| Flag | What it does |
|------|--------------|
| `ls -l` | Detailed listing |
| `ls -a` | Show hidden files |
| `ls -lh` | Human-readable sizes |
| `ls -la` | Detailed + hidden |

---

### 2. `cd` → Change Directory

```bash
cd /etc
```

**Think:** `CHANGE LOCATION`

| Command | Action |
|---------|--------|
| `cd ..` | Parent directory |
| `cd ~` | Home directory |
| `cd /` | Root |
| `cd -` | Previous directory |

---

### 3. `pwd` → Print Working Directory

```bash
pwd
```

**Think:** `WHERE AM I?`

Example output:

```text
/home/ubuntu/projects
```

---

### 4. `cp` → Copy

```bash
cp file.txt backup.txt
```

**Think:** `COPY → original remains`

Copy a directory (recursive):

```bash
cp -r folder/ backup/
```

`-r` → **recursive**

---

### 5. `mv` → Move / Rename

Move:

```bash
mv file.txt /tmp/
```

Rename:

```bash
mv old.txt new.txt
```

**Think:** `MOVE = location change OR rename`

---

### 6. `rm` → Remove

```bash
rm file.txt
```

**Think:** `DELETE`

| Command | What it does |
|---------|--------------|
| `rm -r folder/` | Recursive delete (directory) |
| `rm -rf folder/` | Force + recursive delete |

> ⚠️ **Dangerous:** `rm -rf` recursively and forcefully deletes — no confirmation prompt.

---

### 7. `mkdir` → Make Directory

```bash
mkdir projects
```

Nested directories:

```bash
mkdir -p project/src/main
```

`-p` → create parent directories if needed

---

### 8. `touch` → Create / Timestamp

```bash
touch file.txt
```

- File **doesn't exist** → creates empty file
- File **exists** → updates timestamp

```bash
touch app.log
```

**Think:** `TOUCH → file creation / timestamp`

---

### 9. `find` → Search

Basic search by name:

```bash
find /home -name "file.txt"
```

**Think:** `SEARCH filesystem`

| Filter | Command |
|--------|---------|
| Files only | `find . -type f` |
| Directories only | `find . -type d` |
| By name pattern | `find . -name "*.log"` |

---

### 🧠 30-second revision

```text
ls      → LIST
cd      → CHANGE location
pwd     → WHERE am I?
cp      → COPY
mv      → MOVE / RENAME
rm      → REMOVE
mkdir   → MAKE directory
touch   → CREATE / timestamp
find    → SEARCH
```

### ⭐ Most important flags

```text
ls -la       → detailed + hidden
ls -lh       → human-readable
cp -r        → recursive copy
rm -r        → recursive delete
rm -rf       → force + recursive ⚠️
mkdir -p     → create parents
find -type f → files
find -type d → directories
```

### 🔥 Remember the flow

```text
pwd   → Where am I?
ls    → What's here?
cd    → Go somewhere
mkdir → Create folder
touch → Create file
cp    → Duplicate
mv    → Move / Rename
find  → Search
rm    → Delete
```

## What I built

A keyword-heavy quick-revision guide for the nine core Linux file operations — structured for interview recall and hands-on practice on the terminal.

## What I broke

Nothing — this was a revision-only session.

## Why it broke

N/A

## Architecture decision

Treat terminal navigation as a **repeatable workflow**, not isolated commands:

1. **Orient** → `pwd`, `ls`
2. **Navigate** → `cd`
3. **Create** → `mkdir`, `touch`
4. **Transform** → `cp`, `mv`
5. **Discover** → `find`
6. **Destroy** → `rm` (with caution)

This mirrors how you safely explore and modify any Linux environment — local VM, EC2 instance, or container shell.

## Interview question

> *"What's the difference between `cp` and `mv`? When would you use `rm -rf`, and what risks does it carry? How do you find all `.log` files in the current directory tree?"*

**Answer sketch:** `cp` duplicates (original stays); `mv` changes location or renames. `rm -rf` force-deletes recursively with no prompt — risky on wrong path. Use `find . -name "*.log"` or `find . -type f -name "*.log"`.

## One thing I still don't understand

When to prefer `find` over `locate` / `fd` in production debugging — and how indexing vs live filesystem walks affects performance on large servers.
