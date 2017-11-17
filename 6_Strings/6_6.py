def sentence_reverse(s):
    """
    String -> String
    Given: a sentence string
    Returns: the given sentence with the order of the words reversed
    """
    start, end = 0, 0
    result = []
    s = s[::-1]

    while start < len(s):
        while end < len(s) and s[end] != " ":
            end += 1
        result.append(s[start:end][::-1])
        start, end = end + 1, end + 1
    return " ".join(result)


if __name__ == "__main__":
    assert sentence_reverse("Alice likes Bob") == "Bob likes Alice"
    assert sentence_reverse("Alice likes, Bob!") == "Bob! likes, Alice"
