"""
Processes and analyzes text from a file
"""
from textReader import *

# Constants for word difficulty
EASY = 0
NORMAL = 1
DIFFICULT = 2


def analyzeTextFromFile(filepath: str, wordDifficulties: dict) -> (float, float, float, float, float):
    """ Analyzes the text in the file specified and returns the 5 metrics listed below

        :param filepath: Path to text file to read and analyze
        :param wordDifficulties: Dictionary of words that are either easy, normal or difficult
        :returns: - Average paragraph length measured in sentences <br/>
                  - Average sentence length measured in words <br/>
                  - Percentage of easy words based on the dictionary provided <br/>
                  - Percentage of difficult words based on the dictionary provided <br/>
                  - Percentage of unique words
        """

    # initializing variable to keep track of metrics
    totalNumberOfSentences, totalNumberOfWords = 0, 0
    wordCounter = [0, 0, 0]  # keeps track of number of EASY, NORMAL and DIFFICULT words
    differentWords = []

    # Start by reading the text and split it into its paragraphs
    paragraphs = readParagraphsFromFile(filepath)

    for paragraph in paragraphs:
        # For each paragraph get all sentences
        sentences = getSentences(paragraph)
        totalNumberOfSentences += len(sentences)

        for sentence in sentences:
            # for each sentence get all words
            words = getWords(sentence)
            totalNumberOfWords += len(words)

            for word in words:
                # for all the words, check their difficulty
                wordCounter[getDifficulty(word, wordDifficulties)] += 1
                # If we haven't registered the word before its a new word
                if word not in differentWords:
                    differentWords.append(word)

    # Calculate metrics from values
    averageParagraphLength = totalNumberOfSentences / len(paragraphs)
    averageSentenceLength = totalNumberOfWords / totalNumberOfSentences
    percentEasyWords = wordCounter[EASY] / totalNumberOfWords * 100
    percentDifficultWords = wordCounter[DIFFICULT] / totalNumberOfWords * 100
    percentUniqueWords = len(differentWords) / totalNumberOfWords * 100

    return averageParagraphLength, \
           averageSentenceLength, \
           percentEasyWords, \
           percentDifficultWords, \
           percentUniqueWords


def getDifficulty(word: str, wordDifficulties: dict) -> int:
    """ Checks the words difficulty and returns it

    :param word: Word to find difficulty of
    :param wordDifficulties: Dictionary with words and their associated difficulty
    :return: Difficulty of the word
    """
    if word not in wordDifficulties:
        # Assume words that are not in the dictionary are difficult
        return DIFFICULT
    else:
        # Return the words difficulty
        return wordDifficulties[word]


def createWordDifficultyDictionary(filepath: str) -> dict:
    """ Read the text file and counts the number of occurrences of each word, then assigns a difficulty for each word
    based on how often they appear. A word that appears often is regarded as Easy, and word that rarely appear are
    counted as Difficult. The difficulties are marked by the following values:

    - 0: Easy: the words that are used more often than the average + 50%
    - 1: Normal: words that occur between about average number of times [-50% average +50%]
    - 2: Difficult: the words that are used less than average - 50 %

    The average is calculated by: total number of words / number of unique words

    :param filepath: Path to text file to analyze words from
    :return: Dictionary of all the words in the file, and their difficulty
    """

    # Set limit for what words are considered easy or difficult
    EASY_lowLimit, DIFFICULT_highLimit = 1 + 0.50, 1 - 0.50

    # keep track of words and their number of occurrences in a dictionary
    wordOccurrences = {}
    # Also keep track of total number of words in the file
    totalNumberOfWords = 0

    # Go through entire file and count occurrences of each word
    for paragraph in readParagraphsFromFile(filepath):
        for sentence in getSentences(paragraph):
            for word in getWords(sentence):
                # increase total number of words
                totalNumberOfWords += 1

                # if its a new word add it to the dictionary, if not increase number of occurrences
                if word not in wordOccurrences:
                    wordOccurrences[word] = 1
                else:
                    wordOccurrences[word] = wordOccurrences[word] + 1

    # Calculate average number of occurrences for the words
    averageOccurrences = totalNumberOfWords / len(wordOccurrences)

    # Create difficulty dictionary with all the words
    difficulty = wordOccurrences

    # Go through all the words and set its difficulty based on its number of occurrences
    for word, nrOfOccurrences in wordOccurrences.items():
        if nrOfOccurrences >= EASY_lowLimit * averageOccurrences:
            difficulty[word] = EASY
        elif nrOfOccurrences <= DIFFICULT_highLimit * averageOccurrences:
            difficulty[word] = DIFFICULT
        else:
            difficulty[word] = NORMAL
    return difficulty
