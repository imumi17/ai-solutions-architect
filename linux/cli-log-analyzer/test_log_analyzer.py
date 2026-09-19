import unittest
import tempfile

from log_analyzer import parse_line, analyze_logs


class TestParseLine(unittest.TestCase):

    def test_parse_valid_line(self):
        line = "2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms"

        result = parse_line(line)

        self.assertEqual(result["ip"], "192.168.1.10")
        self.assertEqual(result["method"], "GET")
        self.assertEqual(result["endpoint"], "/api/users")
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["latency"], 120.0)

    def test_parse_invalid_line(self):
        line = "INVALID LOG LINE"

        with self.assertRaises(IndexError):
            parse_line(line)


class TestAnalyzeLogs(unittest.TestCase):

    def test_analyze_logs(self):
        log_content = """\
2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms
2026-09-19 10:00:02 192.168.1.11 GET /api/orders 200 250ms
2026-09-19 10:00:03 192.168.1.12 GET /api/users 500 820ms
"""

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write(log_content)
            filename = file.name

        stats = analyze_logs(filename)

        self.assertEqual(stats["requests"], 3)
        self.assertEqual(stats["errors"], 1)
        self.assertEqual(stats["max_latency"], 820.0)


    def test_malformed_lines(self):
        log_content = """\
2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms
INVALID LOG LINE
2026-09-19 10:00:03 192.168.1.12 GET /api/users 500 820ms
"""

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write(log_content)
            filename = file.name

        stats = analyze_logs(filename)

        self.assertEqual(stats["requests"], 2)
        self.assertEqual(stats["malformed"], 1)
        self.assertEqual(stats["max_latency"], 820.0)

    def test_error_detection(self):
        log_content = """\
2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms
2026-09-19 10:00:02 192.168.1.11 GET /api/orders 404 250ms
2026-09-19 10:00:03 192.168.1.12 GET /api/users 500 820ms
"""

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write(log_content)
            filename = file.name

        stats = analyze_logs(filename)

        self.assertEqual(stats["errors"], 2)

    def test_counters(self):
        log_content = """\
2026-09-19 10:00:01 192.168.1.10 GET /api/users 200 120ms
2026-09-19 10:00:02 192.168.1.10 GET /api/users 200 250ms
2026-09-19 10:00:03 192.168.1.11 GET /api/orders 500 820ms
"""

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as file:
            file.write(log_content)
            filename = file.name

        stats = analyze_logs(filename)

        self.assertEqual(stats["endpoints"]["/api/users"], 2)
        self.assertEqual(stats["endpoints"]["/api/orders"], 1)

        self.assertEqual(stats["ips"]["192.168.1.10"], 2)
        self.assertEqual(stats["ips"]["192.168.1.11"], 1)

        self.assertEqual(stats["status_codes"][200], 2)
        self.assertEqual(stats["status_codes"][500], 1)


    
if __name__ == "__main__":
    unittest.main()