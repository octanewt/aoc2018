#!/usr/bin/env python3
"""."""
from time import strptime, strftime, mktime
from datetime import timedelta, datetime
from itertools import zip_longest

time_format = r'%Y-%m-%d %H:%M'
date_format = r'%m-%d'
min_format = r'%M'


def parse_input(in_file):
    events = {}
    with open(in_file, 'r') as fp:
        for line in fp:
            split_time = line.split('] ', maxsplit=1)
            t = strptime(split_time[0].strip('['), time_format)
            event = split_time[1].strip()
            # print(strftime(time_format, t), event)

            id_split = event.split(' #')
            if len(id_split) > 1:
                guard_id = id_split[1].split()[0]
                events[t] = guard_id
            else:
                if 'falls' in event:
                    events[t] = 'falls'
                elif 'wakes' in event:
                    events[t] = 'wakes'
    sorted_times = sorted(events)
    min_asleep = {}
    guard_dates = {}
    cur_guard = -1
    for st in sorted_times:
        date = strftime(date_format, st)
        if not min_asleep.get(date):
            min_asleep[date] = []
        # print('{}\t{}'.format(strftime(time_format, st), events[st]))
        if events[st] == 'falls':
            time_diff = st.tm_min - len(min_asleep[date])
            min_asleep[date].extend(['.'] * time_diff)
        elif events[st] == 'wakes':
            time_diff = st.tm_min - len(min_asleep[date])
            min_asleep[date].extend(['#'] * time_diff)
        else:
            cur_guard = events[st]
            if not guard_dates.get(cur_guard):
                guard_dates[cur_guard] = []
            if 1 < st.tm_hour < 24:
                gd = datetime(*st[:6]) + timedelta(days=1, hours=-st.tm_hour, minutes=-st.tm_min)
                gd = gd.timetuple()
                # print('{}\t{}'.format(strftime(time_format, st), strftime(time_format, gd)))
            else:
                gd = st
            guard_dates[cur_guard].append(gd)

    return guard_dates, min_asleep


def part_one(in_file):
    guard_dates, min_asleep = parse_input(in_file)
    result = {}
    max_sleep = 0
    for guard in guard_dates:
        # print('#{}'.format(guard))
        date_min_lists = [min_asleep.get(strftime(date_format, x), [])
                          for x in guard_dates[guard]]
        guard_max_sleep_count = 0
        guard_minute = -1
        guard_sleep_total = 0
        for i, minute in enumerate(zip_longest(*date_min_lists, fillvalue='.')):
            sleep_count = minute.count('#')
            guard_sleep_total += sleep_count
            # print('{}\t{}\t{}\t{}'.format(i, ''.join(minute), sleep_count, guard_sleep_total))
            if sleep_count > guard_max_sleep_count:
                guard_max_sleep_count = sleep_count
                guard_minute = i

        if guard_sleep_total > max_sleep:
            max_sleep = guard_sleep_total
            result['guard'] = guard
            result['minute'] = guard_minute

    return result


# result = part_one('input.txt')
# result = part_one('day04_01_input.txt')
#
# for k, v in result.items():
#     print('{}\t\t{}'.format(k, v))
#
# print('result\t\t{}'.format(int(result['guard']) * int(result['minute'])))

# output
# $ time python3 ./day04.py
# guard           1987
# minute          34
# result          67558
#
# real    0m0.108s
# user    0m0.000s
# sys     0m0.000s


def part_two(in_file):
    guard_dates, min_asleep = parse_input(in_file)
    result = {}
    max_sleep = 0
    for guard in guard_dates:
        # print('#{}'.format(guard))
        date_min_lists = [min_asleep.get(strftime(date_format, x), [])
                          for x in guard_dates[guard]]
        guard_max_sleep_count = 0
        guard_minute = -1
        guard_sleep_total = 0
        for i, minute in enumerate(zip_longest(*date_min_lists, fillvalue='.')):
            sleep_count = minute.count('#')
            guard_sleep_total += sleep_count
            # print('{}\t{}\t{}\t{}'.format(i, ''.join(minute), sleep_count, guard_sleep_total))
            if sleep_count > guard_max_sleep_count:
                guard_max_sleep_count = sleep_count
                guard_minute = i

        if guard_max_sleep_count > max_sleep:
            max_sleep = guard_max_sleep_count
            result['guard'] = guard
            result['minute'] = guard_minute

    return result


# result = part_two('input.txt')
result = part_two('day04_02_input.txt')

for k, v in result.items():
    print('{}\t\t{}'.format(k, v))

print('result\t\t{}'.format(int(result['guard']) * int(result['minute'])))

# $ time python3 ./day04.py
# guard           2633
# minute          30
# result          78990
#
# real    0m0.172s
# user    0m0.000s
# sys     0m0.015s
