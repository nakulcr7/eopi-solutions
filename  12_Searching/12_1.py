def search_first_occurence_of_k(array, k):
    low, high = 0, len(array) - 1
    first_k = None
    while low <= high:
        mid = low + (high - low) / 2
        if array[mid] == k:
            first_k = mid
            high = mid - 1
        elif array[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return first_k


def main():
    test_array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    assert search_first_occurence_of_k(test_array, 108) == 3
    assert search_first_occurence_of_k(test_array, 285) == 6


if __name__ == '__main__':
    main()
