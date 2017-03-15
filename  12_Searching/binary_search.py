def binary_search(items, key):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = low + (high - low) / 2
        if items[mid] < key:
            high = mid - 1
        elif items[mid] > key:
            low = mid + 1
        else:
            return mid
    return None


def main():
    test_array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert binary_search(test_array, 108) == 4
    assert binary_search(test_array, 285) == 7
    assert binary_search(test_array, 2) is None
    assert binary_search(test_array, -14) == 0
