# Sorting
Start by reading about sorting algorithms: https://runestone.academy/runestone/books/published/pythonds/SortSearch/toctree.html

The task is to use a sorting algorithm to sort a list of strings (from a data file) by increasing length, and such that strings of the same length are sorted lexicographically.

## Results
If i were to implement this i would have inserted the words in the correct position while reading them from the file, but because the assignment specifically asks to use a sorting algorithm i decided to first implement `bubblesort` which is quick and easy, but as we all know, very slow. So i also implemented `mergesort` as i haven't implemented this sorting algorithm before. As an extra challenge i wanted to see if i could do it without creating any other arrays than the one given (using only in-place swaps).  

I decided to time each sorting algorithm and comparing them that way:
```console
Number of words to sort: 12562 

Bubblesort used: 36 seconds
Mergesort used: 2 seconds
``` 
As we can see, this is quite a big difference. Mergesort being 18 times faster than bubblesort (a difference that just gets bigger as the number of words increase).

After using both algorithms like this: 
```python
bubble = getArrayFromFile("data/Great Expectations.txt")
print("Number of words to sort:", len(bubble), "\n")
bubbleSort(bubble)

merge = getArrayFromFile("data/Great Expectations.txt")
mergeSort(merge)
```
*note that i have to read the array from the file two times, as both algorithms use in-place sorting.*

I get the folowing sorted array back (this is just small excerpts of it):
```console
Array after sorting:
1
2
4
A
B
D
I
J
L
M
O
P
R
T
U
V
X
Z
Ah
Am
An
As
At
Ay
Be
...
Face
Fact
Fail
Fain
Fair
Fall
Fast
Fate
Fear
Feed
Feel
Fees
Feet
Fell
Felt
Fend
File
Fill
Film
Find
Fine
Fire
Firm
Fish
Fist
Fits
Five
Flag
...
Arranging
Arrogance
Artificer
Artifices
Ascertain
Assailant
Assembled
Assenting
Asserting
Assiduity
Assistant
Assisting
Associate
Assurance
Assuredly
Astounded
Attaching
Attempted
Attendant
Attending
Attention
Attentive
Attracted
Audacious
Augmented
Australia
Authority
Available
Avenger’s
Avoidance
Awkwardly
...
Inexplicable
Inflammatory
Ingratitoode
Inhospitable
Inhospitably
Inscriptions
Insinuations
Installation
Instructions
Insufficient
Intellectual
Intelligence
Intelligible
Interchanged
Interference
Interlocutor
Intermediate
Interminable
Interrupting
Interruption
Intervention
Intoxicating
Intoxication
Introduction
Introductory
Invulnerable
...
```
