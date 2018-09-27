import unittest
from suffix_array.suffix_array import SuffixArray


class TestSuffix_array(unittest.TestCase):

    def test_index(self):
        suffix_array = SuffixArray()
        suffix_array.index('banana')
        self.assertEqual(suffix_array.starting_positions, [5, 3, 1, 0, 4, 2])

if __name__ == "__main__":
    unittest.main()
