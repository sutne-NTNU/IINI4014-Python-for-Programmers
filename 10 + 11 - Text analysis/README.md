# Text analysis
There are many ways to analyse text.

Some of those are:
- Number of sentences per paragraph
- Sentence length in words
- Percentage of easy words: easy words are those used frequently: they have high frequency in documents
- Percentage of difficult words: difficult words are those that are seldom used and have low frequency in documents
- Percentage of different words: A count of the unique words in the document divide by the total number of words

Your task is to write a Python code that analyses a text file and returns the measures listed.

Use the first file to create a dictionary (histogram) of the words and their associated frequencies. You can then use the histogram to judge if a word in the second (also from previous assignment) file is easy or difficult.

Note that you can use any text file or use the files attached here.

# Result
The most difficult part of this assignment is the categorization of the difficulty of words.

For this i am using a text file, going over all the words and creating a dictionary of the number of occurrences for each word, i then calculate the expected average number of times word appears in the text (total words/unique words). The dictionary is then altered to only contain the words and their associated difficulty.

How accurate this is could be questioned, we could for instance just use the length of a word instead, or some other metric. The difficulty for each word is in this assignment very reliant on what kind of text we are creating the dictionary from.

## Creating the dictionary of difficulties
```python
dictionaryOfDifficulties = createWordDifficultyDictionary(PATH + "Heart of Darkness.txt")
```
When analyzing a text i can then use this dictionary to check if a word is easy or difficult. If a word isn't in the dictionary i am just going to assume it is a difficult word.

## Testing a small file to verify if numbers seem reasonable
```python
avgParagraphLength, \
avgSentenceLength, \
percentEasyWords, \
percentDifficultWords, \
percentUniqueWords = analyzeTextFromFile(PATH + "Small File.txt", dictionaryOfDifficulties)
print("\n\nSmall File analysis:\n"
      "     %.1f Sentences per paragraph\n"
      "     %.1f Words per sentence\n"
      "     %.1f%% of the words were easy\n"
      "     %.1f%% of the words were difficult\n"
      "     %.1f%% of the words were unique"
      % (avgParagraphLength, avgSentenceLength, percentEasyWords, percentDifficultWords, percentUniqueWords))
```
```console
Small File analysis:
     3.0 Sentences per paragraph
     22.0 Words per sentence
     57.6% of the words were easy
     37.9% of the words were difficult
     66.7% of the words were unique
```

## Analyzing longer texts and comparing them
```console
Great Expectations analysis:
     2.3 Sentences per paragraph
     20.3 Words per sentence
     71.3% of the words were easy
     20.6% of the words were difficult
     6.8% of the words were unique
```
```console
Pride and Prejudice analysis:
     3.0 Sentences per paragraph
     19.2 Words per sentence
     68.5% of the words were easy
     23.6% of the words were difficult
     5.8% of the words were unique
```
