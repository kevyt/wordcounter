from wordcount import Wordcounter
import unittest
from nose2.tools import params


class TestInitWordcounter(unittest.TestCase):
    """Tests __init___"""

    def test_init_with_string(self):
        """Input is parsed."""
        input = "This is a string"
        result = Wordcounter(input)
        self.assertEqual(result.string, "This is a string")

    @params(0, None, ["list", "of", "words"], {"test": "dict"})
    def test_init_other_than_string(self, input):
        """TypeError raised if input not string"""
        with self.assertRaises(TypeError) as error:
            Wordcounter(input)
        self.assertTrue("String must be of type str" in error.exception.args)

    def test_init_empty_string(self):
        """ValueError raised if input empty string"""
        with self.assertRaises(ValueError) as error:
            Wordcounter("")
        self.assertTrue("String must be at least of length 1" in error.exception.args)


class TestWordcounts(unittest.TestCase):
    """Tests _word_counts() method"""

    def test_word_counts_only_string(self):
        """Input is parsed."""
        input = "The sun shines over the lake"
        result = Wordcounter(input)._word_counts()
        self.assertEqual(
            result, {"the": 2, "lake": 1, "over": 1, "shines": 1, "sun": 1}
        )

    def test_word_counts_only_string_cs(self):
        """Input is parsed. Comma seperated"""
        input = "The,sun,shines,over,the,lake"
        result = Wordcounter(input)._word_counts()
        self.assertEqual(
            result, {"the": 2, "lake": 1, "over": 1, "shines": 1, "sun": 1}
        )

    def test_word_counts_with_nums(self):
        """Input is parsed. Numerical is ignored"""
        input = "The sun shines over the 1 lake"
        result = Wordcounter(input)._word_counts()
        self.assertEqual(
            result, {"the": 2, "lake": 1, "over": 1, "shines": 1, "sun": 1}
        )

    def test_word_counts_with_non_word_chars(self):
        """Input is parsed. Other chars are ignored"""
        input = "The sun shines over the #%$#$ lake"
        result = Wordcounter(input)._word_counts()
        self.assertEqual(
            result, {"the": 2, "lake": 1, "over": 1, "shines": 1, "sun": 1}
        )


class TestCalculateFrequencyForWord(unittest.TestCase):
    """Tests calculate_frequency_for_word() method"""

    @params("the", "The", "tHe")
    def test_existing_word_frequency(self, word):
        """Input is parsed. Various cased versions of the"""
        input = "The sun shines over the lake"
        result = Wordcounter(input).calculate_frequency_for_word(word)
        self.assertEqual(result, 2)

    def test_non_existing_word_frequency(self):
        """ValueError is raised when non-existing word is entered"""
        input = "The sun shines over the lake"
        with self.assertRaises(ValueError) as error:
            Wordcounter(input).calculate_frequency_for_word("evil")
        self.assertTrue("Word is not in string" in error.exception.args)


class TestCalculateMostFrequentNWords(unittest.TestCase):
    """Tests calculate_most_frequent_n_words() method"""

    def test_most_frequent_3_words(self):
        """Input parsed. Mind alphabetical order of keys"""
        input = "The sun shines over the lake"
        result = Wordcounter(input).calculate_most_frequent_n_words(3)
        self.assertEqual(result, [("the", 2), ("lake", 1), ("over", 1)])

    def test_most_frequent_100_words(self):
        """Input parsed. Alphabetical order of keys"""
        input = "The sun shines over the lake"
        result = Wordcounter(input).calculate_most_frequent_n_words(100)
        self.assertEqual(
            result, [("the", 2), ("lake", 1), ("over", 1), ("shines", 1), ("sun", 1)]
        )

    @params(0, -1)
    def test_most_frequent_non_positive_n_words(self, n):
        """ValueError raised. Non positive n"""
        input = "The sun shines over the lake"
        with self.assertRaises(ValueError) as error:
            Wordcounter(input).calculate_most_frequent_n_words(n)
        self.assertTrue("n must be a positive integer > 0" in error.exception.args)

    def test_most_frequent_three_words(self):
        """TypeError raised. Non-integer as n"""
        input = "The sun shines over the lake"
        with self.assertRaises(TypeError) as error:
            Wordcounter(input).calculate_most_frequent_n_words("three")
        self.assertTrue("n must be of type int" in error.exception.args)


class TestCalculateHighestFrequency(unittest.TestCase):
    """Tests calculate_highest_frequency() method"""

    def test_highest_frequency_singular(self):
        """Input parsed. Singular most frequent word"""
        input = "The sun shines over the lake"
        result = Wordcounter(input).calculate_highest_frequency()
        self.assertEqual(result, [("the", 2)])

    def test_highest_frequency_multi(self):
        """Input parsed. Multiple most frequent words"""
        input = "The sun shines over the sun lake"
        result = Wordcounter(input).calculate_highest_frequency()
        self.assertEqual(result, [("the", 2), ("sun", 2)])
