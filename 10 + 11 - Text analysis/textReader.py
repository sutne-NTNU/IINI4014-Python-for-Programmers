"""
Reads text from a file into paragraphs and splits text into either words or sentences
"""
import fileinput
import re


def readParagraphsFromFile(filepath: str) -> list:
    """ Reads the entire file and returns a list where each element in the list is a paragraph, a paragraph is
    a block of text separated by blank lines.

    :param filepath: Path to textile to read from
    :return: List of all paragraphs within the file
    """
    paragraphs = []
    currentParagraph = ""
    for line in fileinput.input(filepath):
        if line.strip() == "":
            if currentParagraph != "":
                paragraphs.append(currentParagraph)
                currentParagraph = ""
        else:
            currentParagraph += line + "\n "
    if currentParagraph != "":
        paragraphs.append(currentParagraph)
    return paragraphs


def getSentences(text: str) -> list:
    """ Splits the string into a list where each element in the list is its own sentence. A sentence is recognized
    by being closed with a "."

    :param text: An arbitrary string to separate into its sentences
    :return: List of sentences
    """
    text.replace("\n", " ")
    sentences = text.strip().split(". ")
    # Verify if final entry is an empty string or not (a text usually ends with a .)
    if sentences[len(sentences) - 1] == "":
        sentences.pop(len(sentences) - 1)
    return sentences


def getWords(text: str) -> list:
    """Splits the text into a list where each element in the list is its own word. A word is recognized
    by being separated with a " ". The method also clears the words of all non-charters and capitalizes them.

    :param text: The string to extract the words from
    :return: List of all paragraphs within the file
    """
    words = text.strip().split(" ")
    for i, word in enumerate(words):
        cleanWord = clearWordOfNonCharacters(word)
        words[i] = cleanWord
    return words


def clearWordOfNonCharacters(word: str) -> str:
    """sanitizing the word, also makes all words lowercase and capitalized.
    result is that for instance "NO!" = "No", and "end)." = "End"

    :param word: The word to be sanitized
    :return: The sanitized and capitalized word
    """
    charactersToRemove = ".,:;!?()\"\'*&%”“"
    return re.sub("[" + charactersToRemove + "]", "", word.rstrip()).lower().capitalize()
