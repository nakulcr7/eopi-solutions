def smallest_cyclic_array(array):
    low, high = 0, len(array) - 1
    while low < high:
        mid = low + (high - low) / 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid
    return low


def main():
    test_array = [378, 478, 550, 631, 103, 203, 220, 224, 279, 368]
    assert smallest_cyclic_array(test_array) == 4


if __name__ == '__main__':
    main()
