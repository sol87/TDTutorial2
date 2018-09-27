# coding=utf8
# Copyright (c) 2017 CineUse


def generator_example():
    i = 0
    while True:
        if i % 2 == 1:
            yield i
        elif i > 5:
            return
        i += 1


if __name__ == "__main__":
    x = generator_example()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
