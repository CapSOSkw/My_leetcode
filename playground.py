def is_matched(expr):
    left = '({['
    right = ')}]'

    s = []

    for c in expr:
        if c in left:
            s.append(c)

        elif c in right:
            if s.__len__() == 0:
                return False

            if right.index(c) != left.index(s.pop()):
                return False

    return s.__len__() == 0


if __name__ == '__main__':
    print(is_matched('{()()'))