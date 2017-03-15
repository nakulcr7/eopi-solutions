from collections import defaultdict


def palindrome_possible(s):
    s = [c.lower() for c in s]
    odd_count = 0
    map = defaultdict(int)
    for c in s:
        map[c] += 1
    for c, freq in map.iteritems():
        if freq % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


def main():
    assert palindrome_possible("Lukan") is False
    assert palindrome_possible("abba") is True
    assert palindrome_possible("LluU") is True


if __name__ == '__main__':
    main()
