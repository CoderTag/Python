# You want to keep a limited history of the last few items seen during iteration or duringsome other kind of processing.

from collections import deque
import re


def search(lines, pattern, history=5):

    prev_lines = deque(maxlen=history)
    for line in lines:
        if re.search(pattern, line, re.IGNORECASE):
            yield(line, prev_lines)
        prev_lines.append(line)


if __name__ == '__main__':
    try:
        with open("somefile.txt") as f:
            a = search(f, 'python', history=5)
            for line, prev_lines in a:  # file descriptor is also iterable
                for pline in prev_lines:
                    print(pline, end="")
                print(line, end='')
                print('-' * 20)

    except Exception as e:
        print(e)
