def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n - 1)
        print(n)


def print_num_tail_recursive(n):
    if n > 0:
        print(n)
        print_num_tail_recursive(n - 1)


count = 0


def hanoi_move(n, source, dest, intermediate):
    "将n个盘子通过中介intermediaate从source移动到dest"
    global count

    if n >= 1:  # 递归出口，只剩一个盘子
        hanoi_move(n-1, source, intermediate, dest)
        # print("Move %s -> %s" % (source, dest))
        count += 1
        hanoi_move(n-1, intermediate, dest, source)
    return count


def flattern(rec_list):
    """unpack a nested list to a flat list"""
    for i in rec_list:
        if isinstance(i, list):
            for i in flattern(i):
                yield i
        else:
            yield i


if __name__ == "__main__":
    # print(factorial(5))
    # print_num_recursive(5)
    # print_num_tail_recursive(5)
    print(hanoi_move(20, 'A', 'C', 'B'))
    print(list(flattern([1, [2, 3, [4]]])) == [1, 2, 3, 4])
