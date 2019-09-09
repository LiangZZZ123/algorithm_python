def merge_sort(s):  # not inplace, stable, time: o(nlogn), space: o(n)
    if len(s) <= 1:
        return s
    else:
        mid = int(len(s) / 2)
        left = merge_sort(s[:mid])
        right = merge_sort(s[mid:])

        new_s = merge_sorted_list(left, right)
        return new_s


def merge_sorted_list(sorted_a, sorted_b):
    """
    Merge two sorted list, sorted_a and sorted_b, into one big sorted list
    a: the current index in sorted_a;
    b: the current index in sorted_b
    """
    len_a, len_b = len(sorted_a), len(sorted_b)
    a, b = 0, 0
    new_sorted_list = list()

    while a < len_a and b < len_b:
        # 将下面这个符号改为 <, 就变成了unstable
        if sorted_a[a] <= sorted_b[b]:
            new_sorted_list.append(sorted_a[a])
            a += 1
        else:
            new_sorted_list.append(sorted_b[b])
            b += 1

    # Finally, either sorted_a or sorted_b will be iterated, and we need to add the rest
    # of the other sequence to new_sorted_list
    if a < len_a:
        new_sorted_list.extend(sorted_a[a:])
    else:
        new_sorted_list.extend(sorted_b[b:])

    return new_sorted_list


def test_merge_sort():
    import random
    l1 = list(range(100))
    random.shuffle(l1)
    assert merge_sort(l1) == sorted(l1)


if __name__ == "__main__":
    test_merge_sort()
