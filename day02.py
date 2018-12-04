#!/usr/bin/env python3


# Part 1
def part_one(input_fivale):
    d = {}
    with open(input_fivale, 'r') as fp:
        for id in fp:
            c = {}
            for char in id:
                count = id.count(char)
                c[count] = c.get(count, 0) + 1
            d[2] = d.get(2, 0) + (1 if c.get(2, 0) > 0 else 0)
            d[3] = d.get(3, 0) + (1 if c.get(3, 0) > 0 else 0)

    return d[2] * d[3]


# print('Part 1: %d' % part_one('day02_01_input.txt'))


def diff(a, b):
    count = 0
    place = -1
    for i in range(len(a)):
        if (a[i] is not b[i]):
            place = i
            count += 1

    return (count, place)


def part_two(input_file):
    sameish = {}
    with open(input_file, 'r') as fp:
        for box in fp:
            box = box.strip()
            sameish[box] = []
            for key in sameish:
                key = key.strip()
                difference = diff(key, box)
                if difference[0] == 1 and key not in sameish[box]:
                    sameish[box].append((key, difference[1]))
    return sameish


result_dict = part_two('day02_02_input.txt')
for entry in result_dict:
    if len(result_dict[entry]) == 1:
        sameish = result_dict[entry][0]
        answer = sameish[0][:sameish[1]] + sameish[0][sameish[1]+1:]
        print('"%s" sameish "%s": answer == %s' %
              (entry, result_dict[entry], answer))
    elif len(result_dict[entry]) > 1:
        print('Found one with more than one sameish ids!: %s %s' %
              (entry, result_dict[entry]))
