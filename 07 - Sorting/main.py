import fileinput
import time
import re


def clearWordOfNonCharacters(word):
    charactersToRemove = ".,:;!?()\"\'*&%”“"
    return re.sub("[" + charactersToRemove + "]", "", word.rstrip()).lower().capitalize()


def getArrayFromFile(filepath):
    # Returns array of all unique words within the file
    uniqueWords = []
    for line in fileinput.input(filepath):
        for word in line.rstrip().split(" "):
            word = clearWordOfNonCharacters(word)
            if word != "" and word not in uniqueWords:
                uniqueWords.append(word)
    return uniqueWords


def isCorrect(smallest, largest):
    # returns true if smallest is actually smallest, false otherwise
    # Compare length
    if len(smallest) != len(largest):
        return len(smallest) < len(largest)
    # Compare lexicographically
    return smallest.upper() < largest.upper()


def bubbleSort(array):
    timer = time.time()
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if not isCorrect(smallest=array[j], largest=array[j + 1]):
                # Swap places
                array[j], array[j + 1] = array[j + 1], array[j]
    print("Bubblesort used: %d seconds" % (time.time() - timer))


def mergeSort(array):
    # merge two sorted sub-arrays into one sorted subarray
    # only uses the space of the original array, and one extra temp string variable
    def merge(array, start1, start2, end):
        while start1 < end and start2 <= end:
            # we only need to rearange the array if an item in sub-array 2 is smaller than in in sub-array1
            if not isCorrect(smallest=array[start1], largest=array[start2]):
                # keep track of lowest value as it will be overwritten in the loop after
                temp = array[start2]
                # move items in sub-array1 one spot to the right
                for i in range(start2, start1, -1):
                    array[i] = array[i - 1]
                # insert lowest value in now "free" spot
                array[start1] = temp
                start2 += 1
            start1 += 1

    # Recursive mergestort function
    def _mergeSort(array, start, end):
        if start < end:
            # Split array in two halves
            end1 = (start + end - 1) // 2
            start2 = end1 + 1
            # Sort both halves recursively
            _mergeSort(array, start, end1)
            _mergeSort(array, start2, end)
            # Merge sorted halves
            merge(array, start, start2, end)

    # start timer
    timer = time.time()
    # Sort the array
    _mergeSort(array, 0, len(array) - 1)
    # Print result
    print("Mergesort used: %d seconds" % (time.time() - timer))


if __name__ == '__main__':
    bubble = getArrayFromFile("data/Great Expectations.txt")
    print("Number of words to sort:", len(bubble), "\n")
    bubbleSort(bubble)

    merge = getArrayFromFile("data/Great Expectations.txt")
    mergeSort(merge)

    print("\n\nArray after sorting:")
    for w in merge:
        print(w)
