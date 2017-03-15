from random import randint


def find_kth_largest(array, k):
    low, high = 0, len(array) - 1
    while low <= high:
        pivot = randint(low, high)
        new_pivot = partition_around_pivot(array, low, high, pivot)
        if new_pivot == k - 1:
            return array[new_pivot]
        elif new_pivot < k - 1:
            low = new_pivot + 1
        else:
            high = new_pivot - 1
    return None


def partition_around_pivot(array, low, high, pivot):
    pivot_value = array[pivot]
    new_pivot = low
    array[high], array[pivot] = array[pivot], array[high]
    for i in range(low, high):
        if array[i] > pivot_value:
            array[i], array[new_pivot] = array[new_pivot], array[i]
            new_pivot += 1
    array[high], array[new_pivot] = array[new_pivot], array[high]
    return new_pivot


def main():
    test_array = [3, 2, 1, 5, 4]
    assert find_kth_largest(test_array, 1) == 5
    assert find_kth_largest(test_array, 5) == 1


if __name__ == '__main__':
    main()
