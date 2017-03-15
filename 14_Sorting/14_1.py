def intersection(list_1, list_2):
    intersection = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] == list_2[j] and (i == 0 or list_1[i] != list_1[i - 1]):
            intersection.append(list_1[i])
            i += 1
            j += 1
        elif list_1[i] < list_2[j]:
            i += 1
        else:
            j += 1
    return intersection


def main():
    assert intersection([2, 3, 3, 5, 7, 11], [3, 3, 7, 15, 31]) == [3, 7]


if __name__ == '__main__':
    main()
