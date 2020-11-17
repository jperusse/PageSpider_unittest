import unittest
from utilities.url_utilities import load_urls_from_file
from utilities.url_utilities import load_page
from utilities.url_utilities import scrape_page

def setup():
    print("setup run")

def teardown():
    print("teardown run")

class TestURLUtils(unittest.TestCase):
    def test_read_file_with_urls_missing_file(self):
        urls = load_urls_from_file("missing_file.txt")
        self.assertEqual(len(urls), 0)

    def test_read_file_with_urls_none_in_file(self):
        urls = load_urls_from_file("urls0.txt")
        self.assertEqual(urls, [''])

    def test_read_file_with_urls1(self):
        urls = load_urls_from_file("urls1.txt")
        self.assertEqual(len(urls), 1)

    def test_read_file_with_urls(self):
        urls = load_urls_from_file("urls.txt")
        self.assertGreaterEqual(len(urls), 1)

    def test_load_page(self):
        url1 = "https//:www.google.com"
        page = load_page(url1)
        self.assertTrue(page)

    def test_scrape_page(self):
        url1 = "https//:www.google.com"
        results = scrape_page(page_contents=url1)
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
