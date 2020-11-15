import unittest
from utilities.url_utilities import load_urls_from_file
from utilities.url_utilities import load_page
from utilities.url_utilities import scrape_page


class TestURLUtils(unittest.TestCase):
    def test_read_file_with_urls(self):
        urls = load_urls_from_file("urls.txt")
        self.assertGreaterEqual(len(urls), 1)

    def test_load_page(self):
        page = load_page("https//:www.google.com")
        self.assertTrue(page)

    def test_scrape_page(self):
        results = scrape_page(page_contents="https//:www.google.com")
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
