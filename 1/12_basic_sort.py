import random


def bubble_sort(s):  # inplace, stable, find the biggest in every round
    n = len(s)
    for i in range(n):
        for j in range(n-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    bubble_sort(seq)
    assert seq == sorted_seq


def select_sort(s):  # inplace, unstable,  find the index of the smallest in every round
    n = len(s)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if s[j] < s[min_index]:
                min_index = j
        if min_index != i:
            s[i], s[min_index] = s[min_index], s[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    select_sort(seq)
    assert seq == sorted_seq


def insert_sort(s):  # inplace, stable, find the value of the smallest in every round
    n = len(s)
    for i in range(1, n):
        # value on the i's index in the s should be put in the position's index
        value = s[i]
        position = i
        while position > 0 and value < s[position-1]:
            s[position] = s[position - 1]
            position -= 1
        s[position] = value


def test_insert_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_seq = sorted(seq)
    insert_sort(seq)
    assert seq == sorted_seq
