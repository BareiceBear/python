import random

def random_partition(lst: list, lo: int, hi: int) -> int:
    if hi <= lo:
        return lo
    rd = random.choice(list(range(lo, hi + 1)))
    print("rd", rd)
    flg = lst[rd]
    lst[lo], lst[rd] = lst[rd], lst[lo]
    i, j = lo + 1, hi
    while True:
        while lst[i] < flg:
            if i == hi:
                break
            i += 1

        while lst[j] > flg:
            if j == lo:
                break
            j -= 1
        if i >= j:
            break

        lst[i], lst[j] = lst[j], lst[i]

    lst[lo], lst[j] = lst[j], lst[lo]
    return j


def random_selection(lst: list, lo: int, hi: int, k: int) -> int:
    if lo == hi:
        return lst[lo]
    mid = random_partition(lst, lo, hi)
    print(mid, lst)
    if k == mid - lo + 1:
        return lst[mid]
    elif k < mid - lo + 1:
        return random_selection(lst, lo, mid - 1, k)
    else:
        return random_selection(lst, mid + 1, hi, k - mid + lo - 1)


if __name__ == '__main__':
    lst = [3, 5, 2, 8]
    h = random_selection(lst, 0, len(lst) - 1, 3)
    print(lst)
    print(h)
