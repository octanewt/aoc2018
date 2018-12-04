#! /usr/bin/#!/usr/bin/env python3


# Part 1
def calibrate(changefile):
    result = 0

    with open(changefile) as fp:
        for change in fp:
            result += int(change)
            # print('%s -> %d' % (change.strip(), result))
    return result


# print(calibrate('day01_01_input.txt'))


# Part 2
def find_repeat(changefile):
    result = 0
    d = {}
    while (True):
        with open(changefile) as fp:
            for change in fp:
                result += int(change)
                d[result] = d.get(result, 0) + 1
                if d[result] >= 2:
                    return result


print(find_repeat('day01_02_input.txt'))
