from itertools import groupby


if __name__ == '__main__':
    lines = '''
    This is the
    first paragraph.

    This is the second.
    '''.splitlines()
    for has_chars, frags in groupby(lines, bool):
        if has_chars:
            print(' '.join(frags))
