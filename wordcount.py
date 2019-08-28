import re
from collections import Counter


class Wordcounter:
    """
    Class to count words (non-case senstive) in string.
    
    Input:
    string of words (at least 1 character), seperated by various seperators (space, comma, blank spaces...)
    
    Methods:
       calculate_frequency_for_word(word): compute frequeny (int) of word
       calculate_most_frequent_n_words(n): compute most frequent n words: [(word, frequency)].
       calculate_highest_frequency(): return word with highest frequenct: [(word, frequency)].

    Usage:
    >>> my_word_counter = Wordscounter("This, yes, this, is my sentence")
    >>> most_frequent_10_words = my_word_counter.calculate_most_frequent_n_words(10)
    >>> frequency_of_this = my_word_counter.calculate_frequency_for_word('this')
    >>> highest_frequency = my_word_counter.calculate_highest_frequency()
    """

    def __init__(self, string):
        if type(string) != str:
            raise TypeError("String must be of type str")
        if len(string) == 0:
            raise ValueError("String must be at least of length 1")
        self.string = string

    def __repr__(self):
        if len(self.string) > 20:
            return "{}...".format(self.string[0:17])
        return self.string

    def _word_counts(self):
        """
        Get word counts for only words (no numerical characters) and lowercase them.
        """
        words = re.findall(r"\b[^\d\W]+\b", self.string.lower())
        word_counts = Counter(words)
        return word_counts

    def calculate_frequency_for_word(self, word):
        """
        Calculates the frequency of word in string.
        Returns int (frequency) of requested word.
        """
        word = word.lower()
        if word not in self._word_counts():
            raise ValueError("Word is not in string")
        return self._word_counts()[word]

    def calculate_most_frequent_n_words(self, n):
        """
        Calculates the most frequent n words.
        In the case that several words have the same frequency, words will be returned in alphabetical order.
        Returns list of tuples (word, frequency) of n most frequent words.
        """
        if type(n) != int:
            raise TypeError("n must be of type int")
        if (n < 1):
            raise ValueError("n must be a positive integer > 0")
        word_counts = dict(self._word_counts())
        sorted_word_counts = [
            (word, frequency)
            for word, frequency in sorted(
                word_counts.items(), key=lambda wf: (-wf[1], wf[0])
            )
        ]
        return sorted_word_counts[0:n]

    def calculate_highest_frequency(self):
        """
        Calculates the words with the highest frequency.
        Returns list of tuples (word, frequency) of all words that have the highest frequency.
        """
        highest_frequency = max(self._word_counts().values())
        most_frequent_words = [
            (word, frequency)
            for word, frequency in self._word_counts().items()
            if frequency == highest_frequency
        ]
        return most_frequent_words
