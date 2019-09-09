numbers = list(range(0, 11))


def linear_search(value, iterable):
    for i, v in enumerate(iterable):
        if v == value:
            return i
    return -1


assert linear_search(3, numbers) == 3


def linear_search_v2(func, iterable):
    for i, v in enumerate(iterable):
        if func(v):
            return i
    return -1


assert linear_search_v2(lambda x: x == 5, numbers) == 5


def linear_search_recursive(array, value):
    """从后往前一个个找, 解决了index需要作为nonlocal的问题, 是尾递归"""
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recursive(array[:index], value)


assert linear_search_recursive(numbers, 1) == 1
assert linear_search_recursive(numbers, 10) == 10
assert linear_search_recursive(numbers, 100) == -1
assert linear_search_recursive(numbers, -1) == -1


def linear_search_recursive_v2(array, value):
    """从前往后一个个找, index 需要作为nonlocal, 比较麻烦"""
    index = 0

    def inner(array, value):
        nonlocal index
        if len(array) == 0:
            return -1
        if array[0] == value:
            return index
        index += 1
        return inner(array[1:], value)
    return inner(array, value)


assert linear_search_recursive_v2(numbers, 1) == 1
assert linear_search_recursive_v2(numbers, 2) == 2
assert linear_search_recursive_v2(numbers, 10) == 10
assert linear_search_recursive_v2(numbers, 100) == -1
assert linear_search_recursive_v2(numbers, -1) == -1


def get_first(sorted_array, middle, value):
    """
    Find the index of the first appearance of the value in an array,
    given a known index(which is called "middle") of that value
    """
    # if (sorted_array[middle - 1] == value) and (middle >= 1):
    #     return get_first(sorted_array, middle - 1, value)
    # return middle
    if (sorted_array[middle - 1] != value) or (middle < 1):
        return middle
    return get_first(sorted_array, middle - 1, value)


def binary_search_recursive(sorted_array, begin, end, value):
    """
    :para
        sorted_array
        begin: the beginning position(not value) of the array, usually 0
        end: the ending position of the array(not value), usually len(sorted_array)
        value: the value to find in the array
    :return
        middle: the index of the "value" that appears first in the array
    """
    if begin >= end:
        return -1
    middle = int((begin + end) / 2)
    if sorted_array[middle] == value:
        return get_first(sorted_array, middle, value)
        # return middle
    elif sorted_array[middle] > value:
        return binary_search_recursive(sorted_array, begin, middle, value)
    else:
        return binary_search_recursive(sorted_array, middle+1, end, value)


def test_binary_search_recursive():
    l1 = list(range(10))
    for i in l1:
        assert binary_search_recursive(l1, 0, len(l1), i) == i

    assert binary_search_recursive(l1, 0, len(l1), -1) == -1
    assert binary_search_recursive(l1, 0, len(l1), 10) == -1

    l2 = [1, 1, 1, 1, 1]
    assert binary_search_recursive(l2, 0, len(l2), 1) == 0

    l3 = [1, 1, 2, 2, 3]
    assert binary_search_recursive(l3, 0, len(l3), 2) == 2
