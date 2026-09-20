from trmnl_outside_window import collector
import unittest
from unittest.mock import patch
from trmnl_outside_window.common import ConfigurationError, NoRedirect, clock, packet, push, request


class BoundaryTests(unittest.TestCase):
    def test_demo_fits_and_cannot_be_published(self):
        data = collector.demo(clock({}))
        self.assertLessEqual(len(packet(data)), 2000)
        with patch("trmnl_outside_window.common.request") as network:
            with self.assertRaises(ConfigurationError):
                push(data)
            network.assert_not_called()

    def test_destination_redirect_and_size_guards(self):
        for url in ("http://example.invalid", "https://user:password@example.invalid", "file:///etc/passwd"):
            with self.subTest(url=url), self.assertRaises(ConfigurationError):
                request(url)
        with self.assertRaises(ConfigurationError):
            NoRedirect().redirect_request(None, None, 302, "Found", {}, "https://example.invalid")
        with patch.dict("os.environ", {"TRMNL_WEBHOOK_URL": "https://example.invalid/api/custom_plugins/example"}):
            with patch("trmnl_outside_window.common.request") as network:
                with self.assertRaises(ConfigurationError):
                    push({"title": "Private"})
                network.assert_not_called()
        with self.assertRaises(ConfigurationError):
            packet({"title": "x" * 2000})
        with self.assertRaises(ValueError):
            packet({"value": float("nan")})


if __name__ == "__main__":
    unittest.main()
