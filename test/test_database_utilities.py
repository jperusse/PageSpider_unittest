import unittest
from utilities.database_utilities import create_database
from utilities.database_utilities import save_words_to_database


class TestDBUtils(unittest.TestCase):
    def test_read_file_with_urls(self):
        results = create_database("db_name")
        self.assertTrue(results)

    def test_save_words_to_database(self):
        results = save_words_to_database("word.db", ["word1", "word2"])
        self.assertTrue(results)


if __name__ == '__main__':
    unittest.main()
