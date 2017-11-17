def replace_and_remove(s):
    l = [c for c in s]
    write_i = 0
    a_count = 0

    for c in l:
        if c != 'b':
            l[write_i] = c
            write_i += 1
        if c == 'a':
            a_count += 1

    curr_i = write_i - 1
    l.extend([None] * a_count)
    write_i = write_i + a_count - 1

    while curr_i >= 0:
        if l[curr_i] == 'a':
            l[write_i] = 'd'
            l[write_i - 1] = 'd'
            write_i -= 2
        else:
            l[write_i] = l[curr_i]
            write_i -= 1
        curr_i -= 1
    return [c for c in l if c is not None]


def main():
    assert "".join(replace_and_remove("bacaa")) == 'ddcdddd'
    assert "".join(replace_and_remove("acaa")) == 'ddcdddd'


if __name__ == '__main__':
    main()