def find_nearest_repetition(words):
    map = dict()
    nearest_repeated_dist = float("inf")
    for i, word in enumerate(words):
        if word in map:
            nearest_repeated_dist = min(nearest_repeated_dist, i - map[word])
        map[word] = i
    return nearest_repeated_dist


def main():
    test_list_1 = ['All', 'work', 'and', 'no', 'play', 'makes',
                   'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
    assert find_nearest_repetition(test_list_1) == 2


if __name__ == '__main__':
    main()
