def plus_one(array):
    i = len(array) - 1
    array[i] = array[i] + 1
    while i > 0 and array[i] == 10:
        array[i] = 0
        array[i - 1] = array[i - 1] + 1
        i -= 1
    return array


def main():
    assert plus_one([1, 2, 9]) == [1, 3, 0]


if __name__ == '__main__':
    main()
