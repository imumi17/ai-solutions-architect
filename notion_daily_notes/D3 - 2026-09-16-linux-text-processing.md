---
date: 2026-09-16
title: D3 - 2026-09-16 — Linux Text Processing
topic: Linux Text Processing
notion_page_id: 3dd4fece-88b3-8157-8e4a-cffe066fbc70
notion_page_url: https://app.notion.com/p/3dd4fece88b381578e4acffe066fbc70
---

# D3 - 2026-09-16 — Linux Text Processing

**Date:** September 16, 2026  
**Topic:** Linux Text Processing

## What I learned

### Quick reference — keyword heavy

| Command | Meaning | Remember |
|---------|---------|----------|
| `cat` | **Concatenate / Read** | Display file contents |
| `grep` | **Search text** | Find matching lines |
| `head` | **Beginning** | First N lines |
| `tail` | **End** | Last N lines |
| `sort` | **Sort** | Alphabetical / numeric ordering |
| `uniq` | **Unique** | Remove consecutive duplicates |
| `wc` | **Word Count** | Lines / words / characters |
| `cut` | **Extract columns** | Select fields / characters |
| `sed` | **Stream Editor** | Find / replace / edit text |
| `awk` | **Text Processor** | Columns, filtering, calculations |

---

### 1. `cat` → Read / Concatenate

```bash
cat file.txt
```

**Think:** `READ FILE`

```bash
cat file1.txt file2.txt
```

→ Display both files.

---

### 2. `grep` → Search

```bash
grep "ERROR" app.log
```

**Think:** `SEARCH TEXT → matching lines`

| Flag | What it does |
|------|--------------|
| `grep -i "error" app.log` | Case-insensitive |
| `grep -r "ERROR" /var/log` | Recursive |
| `grep -n "ERROR" app.log` | Show line numbers |
| `grep -v "INFO" app.log` | Exclude matching lines |

---

### 3. `head` → Beginning

```bash
head file.txt
```

→ First **10 lines** by default.

```bash
head -n 5 file.txt
```

→ First 5 lines.

**Think:** `HEAD = START`

---

### 4. `tail` → End

```bash
tail file.txt
```

→ Last **10 lines**.

```bash
tail -n 20 app.log
```

→ Last 20 lines.

#### ⭐ Very important

```bash
tail -f app.log
```

→ **Follow live logs**

**Think:** `TAIL = END / LIVE LOGS`

---

### 5. `sort` → Sort

```bash
sort names.txt
```

→ Alphabetical order.

| Flag | What it does |
|------|--------------|
| `sort -n numbers.txt` | Numeric sorting |
| `sort -r names.txt` | Reverse order |

**Think:** `SORT = ORDER`

---

### 6. `uniq` → Remove Duplicates

```bash
uniq names.txt
```

> ⚠️ `uniq` removes **consecutive** duplicate lines only.

Common combination:

```bash
sort names.txt | uniq
```

→ Sort + remove duplicates.

Even better:

```bash
sort names.txt | uniq -c
```

→ Count occurrences.

**Think:** `UNIQ = DEDUP`

---

### 7. `wc` → Count

```bash
wc file.txt
```

Returns:

```text
lines  words  characters
```

| Flag | What it counts |
|------|----------------|
| `wc -l file.txt` | Lines |
| `wc -w file.txt` | Words |
| `wc -c file.txt` | Bytes |

**Think:** `WC = COUNT`

---

### 8. `cut` → Extract

Used heavily with **CSV / delimited data**.

Example data:

```text
John,25,Bangalore
Sam,30,Delhi
```

```bash
cut -d',' -f1 users.csv
```

Output:

```text
John
Sam
```

- `-d` → **delimiter**
- `-f` → **field / column**

**Think:** `cut → SELECT COLUMN`

---

### 9. `sed` → Stream Editor

Used for **find / replace / editing text**.

```bash
sed 's/old/new/' file.txt
```

→ Replace first occurrence on each line.

| Command | What it does |
|---------|--------------|
| `sed 's/old/new/g' file.txt` | Global replacement |
| `sed '3d' file.txt` | Delete line 3 |

**Think:** `SED = EDIT / SUBSTITUTE`

---

### 10. `awk` → Text Processing

Extremely useful for **columns + filtering + calculations**.

Example data:

```text
John 25 Bangalore
Sam 30 Delhi
```

```bash
awk '{print $1}' users.txt
```

Output:

```text
John
Sam
```

| Variable | Meaning |
|----------|---------|
| `$1` | Column 1 |
| `$2` | Column 2 |
| `$3` | Column 3 |
| `$0` | Entire line |

Filtering:

```bash
awk '$2 > 25 {print $1}' users.txt
```

→ Print names where age > 25.

**Think:** `AWK = FILTER + COLUMNS + CALCULATE`

---

### 🔥 Most important concept: `|` pipe

Text-processing commands become powerful when chained.

```bash
cat app.log | grep ERROR
```

Better:

```bash
grep ERROR app.log | tail -20
```

→ Find errors → show last 20.

Another:

```bash
cat users.txt | sort | uniq -c
```

→ Read → sort → count duplicates.

---

### 🧠 30-second revision

```text
cat    → READ
grep   → SEARCH
head   → FIRST
tail   → LAST / LIVE
sort   → ORDER
uniq   → DEDUP
wc     → COUNT
cut    → COLUMN EXTRACTION
sed    → EDIT / REPLACE
awk    → FILTER / COLUMNS / CALCULATE
```

### ⭐ Remember this progression

```text
READ        → cat
SEARCH      → grep
FIRST/LAST  → head / tail
ORDER       → sort
DEDUP       → uniq
COUNT       → wc
EXTRACT     → cut
EDIT        → sed
ANALYZE     → awk
```

### 🔥 Interview must-know

```bash
grep "ERROR" app.log
tail -f app.log
sort file.txt | uniq -c
wc -l file.txt
cut -d',' -f1 file.csv
sed 's/old/new/g' file.txt
awk '{print $1}' file.txt
```

These commands + **pipes (`|`) + redirection (`>`, `>>`, `<`)** form a huge part of everyday Linux CLI work.

## What I built

A keyword-heavy quick-revision guide for the ten core Linux text-processing commands — with pipe chaining patterns for log analysis and data wrangling.

## What I broke

Nothing — this was a revision-only session.

## Why it broke

N/A

## Architecture decision

Treat the Linux CLI as a **pipeline architecture**:

1. **Source** → `cat` or file input
2. **Filter** → `grep`, `awk`
3. **Transform** → `sort`, `sed`, `cut`
4. **Summarize** → `uniq`, `wc`
5. **Observe** → `head`, `tail`, `tail -f`

Each command does one job well; pipes compose them into powerful one-liners without writing scripts.

## Interview question

> *"How would you find the top 10 most frequent error messages in a log file? How does `tail -f` work, and when would you use `sort | uniq -c`?"*

**Answer sketch:** `grep ERROR app.log | sort | uniq -c | sort -rn | head -10`. `tail -f` streams new lines as they're written — essential for live debugging. `sort | uniq -c` sorts first (required for `uniq`), then counts duplicate lines.

## One thing I still don't understand

When to reach for `awk` vs a short Python script — and how performance compares on multi-GB log files in production.
