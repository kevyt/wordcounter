# Word counter

Class to count words (non case-sensitive) in a given string. Non-alphabetical characters will be ignored.

### Prerequisites

For testing nose2 is used

```
pip install nose2
```

### Usage

Initialise:
```
mywords = Wordcounter("My oh my, this is my sentence!")
```
Count frequency of word:
```
mywords.calculate_frequency_for_word('this')
```
Return most frequent N words:
```
mywords.calculate_most_frequent_n_words()
```
Return most frequent words:
```
mywords.calculate_highest_frequency()
```

## Running the tests

In root run:
```
nose2 -v
```
to get verbose unit test results




## Authors

* **Rick Prins** 

