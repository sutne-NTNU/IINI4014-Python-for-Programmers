"""
Let one of two inputs to a function be any string, e.g. ‘Hello World!’
Let the second input be a vector whose elements are zeros and ones e.g. (0010111).

Write a function that changes the case, upper or lower, of letters in the first string based
on the value of the associated element in the input vector. Specifically, the i-th letter
should be upper case when the i-th element of the binary vector is one.

As an example, given the string ‘Python’ and a binary vector ‘010’, the function should return a new string ‘pYthOn’.
The function should count blank spaces, numbers and special characters without changing them.

Finally, if the binary vector is shorter than the input string then it should be replicated,
i.e. 01 becomes 01+01=0101.
On the other hand, if the vector is shorter than the string it should be truncated.
"""


def example():
    string = 'Python'
    binary_vector = '010'
    print(string_capitalise(string, binary_vector))
    # pYthOn


def string_capitalise(string: str, binary_vector: str) -> str:
    """ Capitalize a string based on the binary vector values

    :param string: string to be capitalized
    :param binary_vector: string of 1 and 0, 1=uppercase and 0=lowercase
    :return: the string capitalized based on the binary vector values
    """
    capitalized_string = ''
    for i, letter in enumerate(string):
        capitalized_string += letter.upper() if binary_vector[i % len(binary_vector)] == '1' else letter.lower()
    return capitalized_string


if __name__ == "__main__":
    example()
