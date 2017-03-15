def int_sq_root(num):
    low, high = 0, num
    while low <= high:
        mid = low + (high - low) / 2
        if mid**2 == num:
            return mid
        elif mid**2 > num:
            high = mid - 1
        else:
            low = mid + 1
    return low - 1


def main():
    assert int_sq_root(5) == 2
    assert int_sq_root(25) == 5


if __name__ == '__main__':
    main()
