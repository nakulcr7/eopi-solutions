def reverse_words(sentence):
    sentence = sentence[::-1]
    list_of_words = sentence.split(' ')
    for i, word in enumerate(list_of_words):
        list_of_words[i] = word[::-1]
    return ' '.join(list_of_words)


def main():
    assert reverse_words("Bob likes Alice") == "Alice likes Bob"


if __name__ == '__main__':
    main()
