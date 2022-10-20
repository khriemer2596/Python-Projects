# Author: Kevin Riemer
# GitHub username: khriemer2596
# Description: Function that shows how long the bubble sort and insertion sort
#              algorithms take to run and plots it using matplotlib.

import time
import random
from matplotlib import pyplot
import functools


def sort_timer(func):
    """Decorator function. Times how many seconds it takes the bubble_sort and insertion_sort functions to run"""
    bubble_time = []
    insertion_time = []

    @functools.wraps(func)
    def sort_timer_wrap(*args, **kwargs):
        """Wrapper function for sort_timer"""
        begin_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - begin_time

        while func.__name__ == "insertion_sort":
            insertion_time.append(total_time)
            return insertion_time

        while func.__name__ == "bubble_sort":
            bubble_time.append(total_time)
            return bubble_time

    return sort_timer_wrap


@sort_timer
def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(dec_func1, dec_func2):
    """
    Randomly generates a list of numbers corresponding to each size in size_thousands. Then creates a copy
    of that list and calls the decorator function to time how long it take the bubble and insertion sort
    to sort the lists. Then plots the results for each size_thousands value.
    """
    size_thousands = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    for size in size_thousands:
        list_1 = []
        for num in range(1, size + 1):
            random_num = random.randint(1, 10000)
            list_1.append(random_num)

        list_2 = list(list_1)

        bubble_data = dec_func1(list_1)
        insertion_data = dec_func2(list_2)

    pyplot.plot(size_thousands, bubble_data, 'bo--', linewidth=2,
                label='Bubble Sort')
    pyplot.plot(size_thousands, insertion_data, 'go--', linewidth=2,
                label='Insertion Sort')
    pyplot.xlabel("Size")
    pyplot.ylabel("Time (s)")
    pyplot.legend(loc='upper left')
    pyplot.show()


compare_sorts(bubble_sort, insertion_sort)

