import unittest
from unittest.mock import MagicMock, patch
from logic import get_url_extension, get_headlines


class LogicUnitTests(unittest.TestCase):
    def test_simple_url(self):
        result = get_url_extension("http://example.com")
        self.assertEqual(result, "com")

    def test_non_string_url(self):
        with self.assertRaises(AssertionError):
            result = get_url_extension(42)


class NYTUnitTests(unittest.TestCase):
    def test_get_headlines(self):
        mock_api_response = MagicMock()
        mock_api_response.json.return_value = {
            "response": {
                "docs": [
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                    {"headline": {"main": "This is a test headline"}},
                ]
            }
        }

        with patch("logic.requests.get") as mock_api_call:
            mock_api_call.return_value = mock_api_response
            result = get_headlines("doesn't matter")
            self.assertEqual(result, ["This is a test headline"] * 10)


if __name__ == "__main__":
    unittest.main()
