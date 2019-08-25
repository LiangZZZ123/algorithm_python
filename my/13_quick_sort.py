def quick_sort(array):  # not inplace; unstable
    size = len(array)
    if not array or size < 2:
        return array
    # pivot_index = 0
    pivot_index = int(len(array) / 2)
    pivot = array[pivot_index]
    # del array[int(pivot_index)]
    left, right = [], []

    for i in range(size):
        if pivot_index != i:
            left.append(array[i]) if array[i] <= pivot else right.append(
                array[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def test_quick_sort():
    import random
    l1 = list(range(100))
    random.shuffle(l1)
    assert quick_sort(l1) == sorted(l1)


def quick_sort_inplace(array, begin, end):
    if begin < end:
        pivot = partition(array, begin, end)
        quick_sort_inplace(array, begin, pivot)
        quick_sort_inplace(array, pivot + 1, end)


def partition(array, begin, end):
    # TODO: Don't know how to do inplace sorting with customizing start-pivot
    pivot_index = begin
    # pivot_index = int(len(array) / 2)
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        while left <= right and array[left] < pivot:
            left += 1
        while right >= left and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]

    return right


def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)) == 3
    l = [1]
    assert partition(l, 0, len(l)) == 0
    l = [2, 1]
    assert partition(l, 0, len(l)) == 1


def test_quick_sort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq


def nth_element(array, begin, end, nth):
    """Find the nth smallest item in an array"""
    if begin < end:
        pivot_index = partition(array, begin, end)
        if pivot_index == nth - 1:
            return array[pivot_index]
        elif pivot_index > nth - 1:
            return nth_element(array, begin, pivot_index, nth)
        else:
            return nth_element(array, pivot_index + 1, end, nth)


def test_nth_element():
    l1 = [3, 5, 4, 2, 1]
    assert nth_element(l1, 0, len(l1), 3) == 3
    assert nth_element(l1, 0, len(l1), 2) == 2

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in l:
        assert nth_element(l, 0, len(l), i) == i
    for i in reversed(l):
        assert nth_element(l, 0, len(l), i) == i

    array = [3, 2, 1, 5, 6, 4]
    assert nth_element(array, 0, len(array), 2) == 2

    array = [2, 1]
    assert nth_element(array, 0, len(array), 1) == 1
    assert nth_element(array, 0, len(array), 2) == 2

    array = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert nth_element(array, 0, len(array), 1) == 3


if __name__ == '__main__':
    test_nth_element()
