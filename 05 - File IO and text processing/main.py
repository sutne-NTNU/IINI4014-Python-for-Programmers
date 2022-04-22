import fileinput
import re


# sanitizing the words to make the dictionairy as clean as possible, also makes all words lowercase and capilized
# result is that for instance "NO!" = "No", and "end)." = "End"
def clearWordOfNonCharacters(word):
    characterToRemove = ".,/()!-\'\""
    return re.sub("[" + characterToRemove + "]", "", word.rstrip()).lower().capitalize()


# Returns a dictionairy with all the words that appear in the file with the amount of times they appear
def getwordfreqs(file):
    dictionary = {}
    for line in fileinput.input(file):
        for word in line.rstrip().split(" "):
            word = clearWordOfNonCharacters(word)
            if word != "":
                if word in dictionary:
                    dictionary[word] = int(dictionary[word]) + 1
                else:
                    dictionary[word] = "1"
    return dictionary


# Returns all line occurences in the file for the specified word
def getwordsline(file, word):
    occurrences = {}
    for (i, line) in enumerate(fileinput.input(file)):
        # only checking for exact words, not partial words i.e "the" doesnt give results for "theory"
        if " " + word.lower() + " " in line.lower():
            occurrences[i + 1] = line.rstrip()
    return occurrences


def main():
    dictionary = getwordfreqs(file="data/Alice’s Adventures in Wonderland.txt")
    for word, occurrences in dictionary.items():
        print('%-16s: %s' % (word, occurrences))

    occurrences = getwordsline(file="data/Great Expectations.txt", word="Mother")
    for occurrence, line in occurrences.items():
        print('%-6s: %s' % (occurrence, line))


if __name__ == "__main__":
    main()
