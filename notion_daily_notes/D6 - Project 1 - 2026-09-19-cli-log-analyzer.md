---
date: 2026-09-19
title: D6 - Project 1 - 2026-09-19 — Weekend Project CLI Log Analyzer
topic: Weekend Project — CLI Log Analyzer
notion_page_id: 3e04fece-88b3-81d6-a6e2-e685ddb1673e
notion_page_url: https://app.notion.com/p/3e04fece88b381d6a6e2e685ddb1673e
---

# D6 - Project 1 - 2026-09-19 — Weekend Project: CLI Log Analyzer

**Date:** September 19, 2026  
**Topic:** Weekend Project — CLI Log Analyzer

**Goal:** Build a production-style Linux CLI tool that reads application logs and generates operational metrics.

## What I learned

### Project overview

**CLI Log Analyzer** — reads `application.log` and produces:

| Output | Description |
|--------|-------------|
| Requests | Total valid log entries |
| Errors | HTTP status ≥ 400 |
| Latency | Average and maximum |
| Top endpoints | Most-hit API paths |
| Top IPs | Most active clients |
| Status-code distribution | Breakdown by HTTP status |

**Location:** `linux/cli-log-analyzer/`

### Project structure

```text
cli-log-analyzer/
├── application.log
├── log_analyzer.py
├── log-analyzer
├── test_log_analyzer.py
├── README.md
└── .gitignore
```

### Sample log format

```text
TIMESTAMP IP METHOD ENDPOINT STATUS_CODE LATENCY
```

Example:

```text
2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms
```

| Field | Example |
|-------|---------|
| Timestamp | `2026-09-19 10:00:01` |
| IP | `192.168.1.10` |
| Method | `GET` |
| Endpoint | `/api/users` |
| Status | `200` |
| Latency | `120ms` |

### Core metrics

**Requests** — total number of valid log entries

**Errors** — HTTP status `>= 400`

**Latency** — average and maximum

**Top endpoints** — e.g. `/api/users`, `/api/orders`, `/api/products`

**Top IPs** — e.g. `192.168.1.10`, `192.168.1.11`

**Status distribution** — e.g. `200 → 5`, `404 → 1`, `500 → 1`

### Python concepts used

```text
File handling    String parsing    split()
Dictionaries     Functions         Counter
Loops            Exception handling  argparse
JSON             unittest
```

### Linux concepts used

```text
cat    grep    wc    sort    |
>      chmod   exit codes
```

Examples:

```bash
grep "500" application.log
grep "500" application.log | wc -l
python3 log_analyzer.py application.log --json > report.json
```

### CLI interface

| Command | Purpose |
|---------|---------|
| `python3 log_analyzer.py application.log` | Basic analysis |
| `--top 5` | Top N endpoints and IPs |
| `--slow 400` | Slow requests (> 400 ms) |
| `--status 500` | Filter by status code |
| `--ip 192.168.1.10` | Filter by IP |
| `--endpoint /api/users` | Filter by endpoint |
| `--json` | JSON output |

Combine filters:

```bash
python3 log_analyzer.py application.log \
    --endpoint /api/users \
    --status 500 \
    --slow 500 \
    --json
```

### Architecture

```text
application.log
       │
       ▼
   Read Lines
       │
       ▼
   Parse Logs
       │
       ▼
Structured Records
       │
       ▼
     Filters
       │
       ▼
   Aggregation
       │
 ┌─────┼─────┬─────┬─────┐
 ▼     ▼     ▼     ▼     ▼
Requests Errors Latency IPs Endpoints
       │
       ▼
    Reports
       │
   ┌───┴───┐
   ▼       ▼
  CLI     JSON
```

### Error handling

| Case | Approach |
|------|----------|
| Malformed log lines | `try/except` → increment `malformed_count` |
| Missing files | `FileNotFoundError` → exit with message |
| Invalid status / latency | Caught by parser exceptions |

```python
try:
    record = parse_line(line)
except (ValueError, IndexError):
    malformed_count += 1
```

### Exit codes

| Code | Meaning |
|------|---------|
| `0` | Success |
| `1` | Failure |

```bash
python3 log_analyzer.py application.log
echo $?   # → 0
```

### Unit testing

Framework: **unittest**

```bash
python3 -m unittest discover
```

Tests cover: valid/invalid parsing, request count, error detection, latency, malformed lines, endpoint/IP/status counters.

Expected: **6 tests, all OK**

### Executable CLI

```bash
chmod +x log-analyzer
./log-analyzer application.log
```

### JSON + Linux pipes

```bash
./log-analyzer application.log --json
./log-analyzer application.log --json > report.json
./log-analyzer application.log --json | jq '.errors'
```

### Git workflow

```bash
git init
git status
git add .
git commit -m "Build CLI log analyzer"
```

### Production concepts practiced

```text
Streaming file processing    Input validation
Data parsing                 Aggregation
Filtering                    CLI design
Exception handling           JSON serialization
Unit testing                 Linux permissions
Exit codes                   Shell scripting
Git                          Documentation
```

### 🔑 Quick revision

```text
Log file → Read → Parse → Validate → Filter → Aggregate → Analyze → CLI / JSON
```

**Must remember:**

| Concept | Use |
|---------|-----|
| `Counter` | Frequency analysis |
| `argparse` | CLI arguments |
| `try/except` | Error handling |
| `unittest` | Automated testing |
| `json` | Machine-readable output |
| `chmod +x` | Executable permission |
| `$?` | Previous command exit code |
| `\|` | Pipe commands |
| `>` | Redirect output |

**Final project outcome:**

```text
Raw Logs → Python Parser → Validated Records → Analytics → CLI Report → JSON → Linux Automation
```

**D6 objective:** Learn the complete pattern of **raw operational data → parsing → validation → aggregation → analysis → automation**.

## What I built

A full **CLI Log Analyzer** weekend project under `linux/cli-log-analyzer/` — Python parser, bash wrapper, unit tests, sample log, README with architecture docs, and Git integration.

## What broke

Nothing critical during build — malformed lines are handled gracefully by design.

## Why it broke

N/A — intentional error handling for bad log lines and missing files.

## Architecture decision

**Single-pass streaming pipeline** with no external dependencies:

1. Read log line-by-line (memory-efficient)
2. Parse into structured records
3. Apply optional filters (`--status`, `--ip`, `--endpoint`, `--slow`)
4. Aggregate with `Counter` for top-N queries
5. Output human CLI report or JSON for automation

This mirrors how real observability tools process logs at scale.

## Interview question

> *"Walk me through how you'd build a CLI tool that analyzes application logs and outputs top endpoints, error counts, and latency metrics."*

**Answer sketch:** Stream the file line-by-line, parse each entry into a dict, skip malformed lines, use `Counter` for frequency stats, compute aggregates in one pass, expose via `argparse` with filter flags, output CLI or JSON, add `unittest` coverage, wrap with a bash executable.

## One thing I still don't understand

How to scale this pattern to multi-GB log files — chunked processing, mmap, or pushing aggregation to something like Elasticsearch/Fluentd instead of in-memory counters.
