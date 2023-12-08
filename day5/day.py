import sys
import pdb
import threading

TEST1_ANSWER = 35
TEST2_ANSWER = 46


DST = 0
SRC = 1
OFF = 2


def main():
    with open('testinput1.txt') as f:
        lines = f.readlines()
        result = part1(lines)
        if result == TEST1_ANSWER:
            print("Test passed, continuing...")
        else:
            print("Test failed, \
                    expected: {}, actual: {}".format(TEST1_ANSWER, result))

    with open('testinput2.txt') as f:
        lines = f.readlines()
        result = part2(lines)
        if result == TEST2_ANSWER:
            print("Test passed, continuing...")
        else:
            print("Test failed, \
                    expected: {}, actual: {}".format(TEST2_ANSWER, result))

    if '--test' not in sys.argv:
        with open('input.txt') as f:
            lines = f.readlines()

            print("Part 1:", part1(lines))
            print("Part 2:", part2(lines))


def part1(lines):
    seeds = [eval(i) for i in lines[0].split(': ')[1].split(' ')]

    range_types = {
            'sts': [],
            'stf': [],
            'ftw': [],
            'wtl': [],
            'ltt': [],
            'tth': [],
            'htl': []
    }

    curr_range = ''

    for line in lines:
        if 'map' in line:
            for rt in range_types:
                curr_range = rt if len(range_types[rt]) == 0 else ''
                if curr_range != '':
                    break
        elif 'seeds' in line:
            pass
        elif line != '\n' and curr_range != '':
            split_line = [eval(i) for i in line.split(' ')]
            range_types[curr_range].append(tuple(split_line))

    min_val = float('inf')
    for seed in seeds:
        temp_val = seed
        for rt in range_types:
            temp_val = convert_to(temp_val, range_types[rt])
        if temp_val < min_val:
            min_val = temp_val

    return min_val


def part2(lines):
    seeds = [eval(i) for i in lines[0].split(': ')[1].split(' ')]

    seed_ranges = []
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            seed_ranges.append(tuple([seed]))
        else:
            seed_ranges[-1] += (tuple([seed]))

    min_val = float('inf')
    for i, sr in enumerate(seed_ranges):
        seeds = []
        x = threading.Thread(target=multithreaded_seeds_from_ranges, args=(sr, seeds))
        x.start()
        x.join()

        range_types = {
                'sts': [],
                'stf': [],
                'ftw': [],
                'wtl': [],
                'ltt': [],
                'tth': [],
                'htl': []
        }

        curr_range = ''

        for line in lines:
            if 'map' in line:
                for rt in range_types:
                    curr_range = rt if len(range_types[rt]) == 0 else ''
                    if curr_range != '':
                        break
            elif 'seeds' in line:
                pass
            elif line != '\n' and curr_range != '':
                split_line = [eval(i) for i in line.split(' ')]
                range_types[curr_range].append(tuple(split_line))

        for seed in seeds:
            temp_val = seed
            for rt in range_types:
                temp_val = convert_to(temp_val, range_types[rt])
            if temp_val < min_val:
                min_val = temp_val

    return min_val


def convert_to(val, ranges):
    for r in ranges:
        if val >= r[SRC] and val < r[SRC]+r[OFF]:
            return r[DST] + (val - r[SRC])
    return val


def multithreaded_seeds_from_ranges(seed_range, seeds):
    for i in range(seed_range[0], seed_range[0]+seed_range[1]):
        seeds.append(i)


if __name__ == '__main__':
    main()
