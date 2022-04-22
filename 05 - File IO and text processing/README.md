# File I/O and text processing
#### Introduction
In this assignment we will learn about navigating the file system, file I/O, and efficient use of lists and dictionaries.

This assignment is broken up into two tasks.

- Write a function getwordfreqs() that takes a filename as input and returns a dictionary of words and their frequencies.
- Write a function getwordsline() that takes as input a file name and a word (string) and returns a list of the line numbers were the word is found.
The zip file contains folders with text files for experimenting.

Reading material: https://docs.python.org/3/library/filesys.html
## Result
Here is an excerpt from the dictionary you get when using the function like this:
```python
dictionary = getwordfreqs(file="data/Alice’s Adventures in Wonderland.txt")
```
```console
Alice’s         : 17
Adventures      : 10
In              : 414
Wonderland      : 8
By              : 76
Lewis           : 4
Carroll         : 4
This            : 169
Ebook           : 8
Is              : 114
For             : 167
The             : 1781
Use             : 29
Of              : 610
Anyone          : 5
Anywhere        : 3
...

```
<br/>
And here is the result of the second function used like this:

```python
occurences = getwordsline(file="data/Great Expectations.txt", word="Mother")
```
```console
60    : my mother was freckled and sickly. To five little stone lozenges, each
1823  : “‘Consequence, my mother and me we ran away from my father several
1824  : times; and then my mother she’d go out to work, and she’d say, “Joe,”
4690  : “You’re a foul shrew, Mother Gargery,” growled the journeyman. “If that
6297  : and the hosier’s, and felt rather like Mother Hubbard’s dog whose outfit
7370  : know, was a spoilt child. Her mother died when she was a baby, and her
8339  : Startop had been spoilt by a weak mother and kept at home when he
11163 : “No; there are only two; mother and daughter. The mother is a lady of
12371 : pink, and the daughter’s was yellow; the mother set up for frivolity,
15025 : married soon. Why do you injuriously introduce the name of my mother by
15509 : her motherly help. For, Clara has no mother of her own, Handel, and no
15515 : But what a blessing it is for the son of my father and mother to love a
16813 : “Now, whether,” pursued Herbert, “he had used the child’s mother ill, or
16814 : whether he had used the child’s mother well, Provis doesn’t say; but she
16960 : “I have seen her mother within these three days.”
17127 : the mother was still living. That the father was still living. That the
```
