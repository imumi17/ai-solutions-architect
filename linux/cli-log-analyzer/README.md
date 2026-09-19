# CLI Log Analyzer

A lightweight Linux command-line tool for analyzing application logs and
generating operational metrics such as request volume, errors, latency,
top endpoints, top IPs, and HTTP status-code distribution.

## Features

- Parse application logs line-by-line
- Calculate total requests
- Detect HTTP errors
- Calculate average latency
- Identify maximum latency
- Find top API endpoints
- Find top client IPs
- Analyze HTTP status-code distribution
- Detect malformed log entries
- Filter by HTTP status
- Filter by IP address
- Filter by endpoint
- Identify slow requests
- Limit top-N results
- JSON output for automation
- Graceful file-error handling
- Automated unit tests

## Log Format

The analyzer expects logs in the following format:

TIMESTAMP IP METHOD ENDPOINT STATUS_CODE LATENCY

Example:

2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms

## Usage

### Basic analysis

```bash
./log-analyzer application.log
