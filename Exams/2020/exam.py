import functools  # To use timeit on functions more easily

import numpy as np
import matplotlib.pyplot as plt
import timeit
import statistics  # for mean, standard deviation and variance


def main():
    n = 1_000
    # create numpy array filled with random floats between the limits, of size n
    num_list = np.random.uniform(size=n)
    # copy these values to a python list
    p_list = num_list.copy().tolist()

    # Sort these lists while using timeit to check the sorting times
    ascending_p_list, ascending_num_list = [], []
    descending_p_list, descending_num_list = [], []
    my_quicksort_p_list, my_quicksort_num_list = [], []

    number_of_tests = 100
    for i in range(number_of_tests):
        """
        For all the test all the sorting are done on the exact same values, 
        however for each test, the values are randomized.
        """

        # time ascending sort of both list with built in functions
        p_list_copy = p_list.copy()
        ascending_p_list.append(timeit.timeit(functools.partial(list.sort, p_list_copy), number=1))
        ascending_num_list.append(timeit.timeit(functools.partial(np.sort, num_list), number=1))

        # when using the built-in functions i am not changing the values in the actual array so i dont have to
        # randomize before sorting in descending,or using my quicksort (otherwise the array would already be sorted)

        # time descending sort of both list with built in functions
        p_list_copy = p_list.copy()
        descending_p_list.append(timeit.timeit(functools.partial(list.sort, p_list_copy, reverse=True), number=1))
        # numpy does not sort descending, so sort and then reverse the sorted array
        np_reverse_sort = lambda: np.sort(num_list)[::-1]
        descending_num_list.append(timeit.timeit(np_reverse_sort, number=1))

        # time my implementation of quicksort on both lists
        my_quicksort_p_list.append(timeit.timeit(functools.partial(quickSort, p_list), number=1))
        my_quicksort_num_list.append(timeit.timeit(functools.partial(quickSort, num_list), number=1))

        # Randomizing the num_list
        randomize(num_list)
        # Copy this to p_list so lists are identical
        p_list = num_list.copy().tolist()

    # Plot sorting time for each test
    plot((ascending_p_list, 'ascending: p_list'),
         (ascending_num_list, 'ascending: num_list'),
         (descending_p_list, 'descending: p_list'),
         (descending_num_list, 'descending: num_list'),
         (my_quicksort_p_list, 'my quicksort: p_list'),
         (my_quicksort_num_list, 'my quicksort: num_list'),
         title='Sorting times', labels=('Test nr', 'Sorting time in seconds (logarithmic scale)'), plot_type='.')

    # Plot the histograms for each of the running times,
    """ i would have put these plots in the same figure and used subplots, but i ran out of time """
    axis_labels = ('Time in seconds', 'Number per bin')
    plot_histogram(ascending_p_list, title='Ascending p_list', labels=axis_labels)
    plot_histogram(ascending_num_list, title='Ascending num_list', labels=axis_labels)
    plot_histogram(descending_p_list, title='Descending p_list', labels=axis_labels)
    plot_histogram(descending_num_list, title='Descending num_list', labels=axis_labels)
    plot_histogram(my_quicksort_p_list, title='Quicksort p_list', labels=axis_labels)
    plot_histogram(my_quicksort_num_list, title='Quicksort num_list', labels=axis_labels)


def randomize(array):
    """ Randomizes the order of items in the array

    :param array: Array of items to be randomized
    """
    for i in range(len(array)):
        # find new random index that is not equal to the original
        new_index = i
        while new_index == i:
            new_index = np.random.randint(low=0, high=len(array) - 1)
        # swap items at these indices
        array[i], array[new_index] = array[new_index], array[i]


def plot(*args, title: str, labels: tuple, **kwargs) -> None:
    """ Plots values according to the specifications given

    :param title: Title of the plot
    :param labels: (x label, y label), labels for the axis
    """
    # default values
    plot_type, color = '-', 'blue'
    # Adjust plot according to keyword arguments
    for key, value in kwargs.items():
        if key == 'xlim':
            plt.xlim(value)
        elif key == 'ylim':
            plt.ylim(value)
        elif key == 'plot_type':
            plot_type = value

    # Plot the values
    plt.title(title)
    xLabel, yLabel = labels
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.yscale('log')
    for argument in args:
        values, label = argument
        plt.plot(values, plot_type, label=label)
    plt.legend()
    plt.show()


def plot_histogram(values, title: str, labels: tuple) -> None:
    """ Plots a histogram of the values, including mean, standard deviations and variance

    :param values: list or one-dimensional numpy array to be plotted
    :param title: Title of the plot
    :param labels: (x label, y label), labels for the axis
    """
    # plot mean value as a red line
    line_height = 60
    mean = statistics.mean(values)
    plt.vlines(mean, 0, line_height, label='Mean: %.6f seconds' % mean, colors='red')

    # plot standard deviations from mean
    standard_deviation = statistics.stdev(values)
    color = '0.65'  # gray
    plt.vlines(mean + 1 * standard_deviation, 0, line_height, label='Standard deviations from mean', colors=color)
    plt.vlines(mean - 1 * standard_deviation, 0, line_height, colors=color)
    plt.vlines(mean + 2 * standard_deviation, 0, line_height, colors=color)
    plt.vlines(mean - 2 * standard_deviation, 0, line_height, colors=color)
    plt.vlines(mean + 3 * standard_deviation, 0, line_height, colors=color)
    plt.vlines(mean - 3 * standard_deviation, 0, line_height, colors=color)

    # Plot the values
    """ add variance to title because i dont have time to add text within figure in a decent way """
    plt.title(title + '     - Variance: ' + str(statistics.variance(values)))
    xLabel, yLabel = labels
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.hist(values, bins=20)
    plt.legend()
    plt.show()


# Python program for implementation of Quicksort inspired by:
# https://www.geeksforgeeks.org/python-program-for-quicksort/
def quickSort(array, low=None, high=None):
    """ Sorts the given array between the two indices, if no indices are given sorts entire array

    :param array: Array to be sorted
    :param low: Starting index
    :param high: Ending index
    """

    def partition(low, high):
        """ This function takes last element as pivot, places the pivot element at its correct position in sorted
        array, and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot

        :param low:
        :param high:
        :return: index of pivot
        """
        i = (low - 1)  # index of
        pivot_value = array[high]

        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if array[j] <= pivot_value:
                # increment index of smaller element
                i = i + 1
                array[i], array[j] = array[j], array[i]

        pivot_index = i + 1
        # Swap pivot to correct position
        array[pivot_index], array[high] = array[high], array[pivot_index]
        return pivot_index

    # if indices arent given, sort entire array
    low = low if low is not None else 0
    high = high if high is not None else len(array) - 1

    if len(array) == 1:
        return array
    if low < high:
        # pivot is partitioning index, arr[p] is now at right place
        pivot = partition(low, high)
        # Separately sort elements before partition and after partition
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)


if __name__ == "__main__":
    main()
    """
    About the results:
    
    As we can see from the graphs, numpy arrays are the fastest to sort with its built-in functions. However it
    looks like regular python lists are quicker to sort using my implementation of the Quicksort Algorithm.
    
    """
