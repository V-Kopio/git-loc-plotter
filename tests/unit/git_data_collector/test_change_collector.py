import unittest
from sample.git_data_collector import change_collector

class TestChangeCollector(unittest.TestCase):

    def test_input_with_plural_insertion_and_deletions(self):
        data = change_collector(' 5 files changed, 2 insertions(+), 3 deletions(-)')

        self.assertEqual(5, data["files"])
        self.assertEqual(2, data["insertions"])
        self.assertEqual(3, data["deletions"])

    def test_input_with_singular_insertion_and_deletions(self):
        data = change_collector(' 1 file changed, 1 insertion(+), 1 deletion(-)')

        self.assertEqual(1, data["files"])
        self.assertEqual(1, data["insertions"])
        self.assertEqual(1, data["deletions"])

    def test_input_with_deletions(self):
        data = change_collector(' 1 file changed, 3 deletions(-)')

        self.assertEqual(1, data["files"])
        self.assertEqual(0, data["insertions"])
        self.assertEqual(3, data["deletions"])

    def test_input_with_insertion(self):
        data = change_collector(' 1 file changed, 2 insertions(+)')

        self.assertEqual(1, data["files"])
        self.assertEqual(2, data["insertions"])
        self.assertEqual(0, data["deletions"])

    def test_input_with_only_files(self):
        data = change_collector(' 1 file changed')

        self.assertEqual(1, data["files"])
        self.assertEqual(0, data["insertions"])
        self.assertEqual(0, data["deletions"])

if __name__ == '__main__':
    unittest.main()
