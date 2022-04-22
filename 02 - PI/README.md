# Calculation of PI
From the time of the Babylonians, mathematicians have known that the circumference of a circle is slightly more than three times its diameter.

Since then, people have been estimating pi with increasing accuracy but because pi is not a rational number it is impossible to define it without some error.

One of the oldest methods to estimate pi was proposed by the great mathematician Archimedes.

In this assignment, you are asked to write code to estimate pi using Archimedes method.

You can find a nice description of the method with implementation in excel here:

https://www.youtube.com/watch?v=_rJdkhlWZVQ&pbjreload=10

 

## Requirements:

The calculation of PI should be defined as a function,

Use descriptive names for the variables and the function, e.g.

def ArchimedesPI():

Read the extra reading material about iter, iteration and iterable.

## Result
Using the function like this:
```python
pi = archimedesPI(number_of_correct_decimals=5)  
print("Calculated value of pi:", pi)
```
yields the following result:
```console
6144 sides needed for 5 correct decimal places.
Calculated value of pi: 3.14159
```