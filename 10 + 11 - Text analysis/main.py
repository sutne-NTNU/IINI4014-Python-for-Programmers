from textAnalyzer import *

PATH = "./data/"

if __name__ == "__main__":
    # Create dictionary of easy and difficult words
    dictionaryOfDifficulties = createWordDifficultyDictionary(PATH + "Heart of Darkness.txt")

    # Test on small file to verify if numbers are reasonable
    avgParagraphLength, \
    avgSentenceLength, \
    percentEasyWords, \
    percentDifficultWords, \
    percentUniqueWords = analyzeTextFromFile(PATH + "Small File.txt", dictionaryOfDifficulties)
    print("Small File analysis:\n"
          "     %.1f Sentences per paragraph\n"
          "     %.1f Words per sentence\n"
          "     %.1f%% of the words were easy\n"
          "     %.1f%% of the words were difficult\n"
          "     %.1f%% of the words were unique"
          % (avgParagraphLength, avgSentenceLength, percentEasyWords, percentDifficultWords, percentUniqueWords))

    # Analyze the first text
    avgParagraphLength, \
    avgSentenceLength, \
    percentEasyWords, \
    percentDifficultWords, \
    percentUniqueWords = analyzeTextFromFile(PATH + "Great Expectations.txt", dictionaryOfDifficulties)

    print("\n\nGreat Expectations analysis:\n"
          "     %.1f Sentences per paragraph\n"
          "     %.1f Words per sentence\n"
          "     %.1f%% of the words were easy\n"
          "     %.1f%% of the words were difficult\n"
          "     %.1f%% of the words were unique"
          % (avgParagraphLength, avgSentenceLength, percentEasyWords, percentDifficultWords, percentUniqueWords))

    # Analyze the second text
    avgParagraphLength, \
    avgSentenceLength, \
    percentEasyWords, \
    percentDifficultWords, \
    percentUniqueWords = analyzeTextFromFile(PATH + "Pride and Prejudice.txt", dictionaryOfDifficulties)

    print("\n\nPride and Prejudice analysis:\n"
          "     %.1f Sentences per paragraph\n"
          "     %.1f Words per sentence\n"
          "     %.1f%% of the words were easy\n"
          "     %.1f%% of the words were difficult\n"
          "     %.1f%% of the words were unique"
          % (avgParagraphLength, avgSentenceLength, percentEasyWords, percentDifficultWords, percentUniqueWords))
