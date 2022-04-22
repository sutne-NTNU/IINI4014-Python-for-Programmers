"""
Matrix multiplication by Hadamard product

Write a function that takes two 2-dimensional arrays a, b, and returns the matrix multiplication by
Hadamard product in a new 2-dimensional array x.

Hadamard product: x(i,j) = a(i,j) * b(i,j)

For any resulting value x(i,j) > 255, set x(i,j) = 255.
"""


def hadamard_product(a: list, b: list) -> list:
    """ Find the Hadamard product of two matrices (two-dimensional arrays/lists)

    :param a: two dimensional list
    :param b: two dimensional list of same dimensions as a
    :return: Hadamard product of the arrays
    """
    if not len(a) == len(b) or not len(a[0]) == len(b[0]):
        raise Exception('The arrays must have the same dimensions')
    # create result array of same size as 'a' (all values are overwritten)
    x = a
    for i in range(len(a)):  # i = row
        for j in range(len(a[0])):  # j = column
            x[i][j] = min(255, a[i][j] * b[i][j])
    return x


def example():
    a = [[5, 10, 15],
         [10, 15, 5]]

    b = [[15, 5, 10],
         [30, 10, 15]]

    x = hadamard_product(a, b)

    for row in x:
        print(row)
        # [ 75,  50, 150]
        # [255, 150,  75]


if __name__ == "__main__":
    example()
