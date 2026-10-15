
import unittest

from meaning_explorer import get_related_words


class TestMeaningExplorer(unittest.TestCase):

    def test_returns_five_words_by_default(self):
        words = get_related_words("king")
        self.assertEqual(len(words), 5)

    def test_returns_requested_number_of_words(self):
        words = get_related_words("king", topn=3)
        self.assertEqual(len(words), 3)

    def test_case_insensitive(self):
        self.assertEqual(
            get_related_words("KING"),
            get_related_words("king")
        )

    def test_strips_whitespace(self):
        self.assertEqual(
            get_related_words("  king  "),
            get_related_words("king")
        )

    def test_unknown_word(self):
        self.assertEqual(
            get_related_words("xyzabc123"),
            []
        )

    def test_empty_input(self):
        self.assertEqual(get_related_words(""), [])

    def test_whitespace_only_input(self):
        self.assertEqual(get_related_words("   "), [])


if __name__ == "__main__":
    unittest.main()
