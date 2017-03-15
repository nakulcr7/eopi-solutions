def is_palindromic(s):
    l = [c.lower() for c in s if c.isalnum()]
    i = 0
    j = len(l) - 1

    while i < j:
        if l[i] != l[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    assert is_palindromic("Ray is ray") is False
    assert is_palindromic("Able was I, ere I saw Elba") is True


if __name__ == '__main__':
    main()
