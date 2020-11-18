import unittest
from utilities.url_utilities import load_urls_from_file
from utilities.url_utilities import load_page
from utilities.url_utilities import scrape_page


class TestURLUtils(unittest.TestCase):
    def setUp(self):
        urls = []
        self.url1 = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    def tearDown(self):
        pass

    def test_read_file_with_urls_missing_file(self):
        self.urls = load_urls_from_file("missing_file.txt")
        self.assertEqual(0, len(self.urls))

    def test_read_file_with_urls_none_in_file(self):
        self.urls = load_urls_from_file("urls0.txt")
        self.assertEqual([], self.urls)

    def test_read_file_with_urls1(self):
        urls = load_urls_from_file("urls1.txt")
        self.assertEqual(1, len(urls))

    def test_read_file_with_urls(self):
        urls = load_urls_from_file("urls.txt")
        self.assertEqual(2, len(urls))

    def test_load_page(self):
        html = load_page(self.url1)
        self.assertTrue(html)

    def test_scrape_page(self):
        html = load_page(self.url1)
        results = scrape_page(page_contents=html)
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
