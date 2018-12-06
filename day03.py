#!/usr/bin/env python3
"""."""


class Claim(object):
    """docstring for Claim."""

    def __init__(self, claim_str, **kwargs):
        """."""
        if claim_str:
            r = self._parse_str(claim_str)
            self.claim_id = (int)(r['claim_id'])
            self.startx = (int)(r['start'][0])
            self.starty = (int)(r['start'][1])
            self.width = (int)(r['dimensions'][0])
            self.height = (int)(r['dimensions'][1])
        elif kwargs:
            self.claim_id = (int)(kwargs['claim_id'])
            self.startx = (int)(kwargs['startx'])
            self.starty = (int)(kwargs['starty'])
            self.width = (int)(kwargs['width'])
            self.height = (int)(kwargs['height'])
        else:
            raise ValueError('invalid args to init')

        self.coord_set = self._coords()

    def _parse_str(self, claim_str):
        r = {}
        id_split = claim_str.split(' @ ')
        r['claim_id'] = id_split[0].strip('#')

        start_split = id_split[1].split(': ')
        r['start'] = start_split[0].split(',')

        r['dimensions'] = start_split[1].strip().split('x')
        return r

    def _coords(self):
        result = set()
        for i in range(self.startx, self.startx + self.width):
            for j in range(self.starty, self.starty + self.height):
                result.add((i, j))
        return result

    def inside(self, other):
        if self.claim_id == other.claim_id:
            return 0
        result = self.coord_set & other.coord_set
        # print('{}:{}  =>  {}'.format(self.claim_id, other.claim_id, result))
        return len(result)


def part_one(in_file):
    result = 0
    with open(in_file, 'r') as fp:
        coord_map = {}
        for c in fp:
            claim = Claim(c)
            for i in range(claim.startx, claim.startx + claim.width):
                for j in range(claim.starty, claim.starty + claim.height):
                    coord = (i, j)
                    coord_map[coord] = coord_map.get(coord, 0) + 1
    # print(coord_map)
    coord_map = {k: v for k, v in coord_map.items() if v > 1}
    # print(coord_map)
    result = len(coord_map)

    return result


# print(part_one('day03_01_input.txt'))
# answer: 103482


def part_two(in_file):
    """."""
    result = 0
    with open(in_file, 'r') as fp:
        coord_map = {}
        claim_list = [Claim(c) for c in fp]
        for c in claim_list:
            coord_map[c.claim_id] = []
            for d in claim_list:
                if c.inside(d):
                    coord_map[c.claim_id].append(d.claim_id)
    result = [c for c in coord_map if coord_map[c] == []]
    if len(result) > 1:
        raise Exception('Too many results!: {}'.format(result))
    elif not result:
        raise Exception('No results!: {}'.format(result))
    return result[0]


print(part_two('day03_02_input.txt'))
# answer: 686
# print(part_two('input.txt'))
