import sys
import re

TEST1_ANSWER = 288
TEST2_ANSWER = 71503


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
    times = [eval(i) for i in re.split(r'\s+', lines[0].split(':')[1].strip())]
    distances = [eval(i) for i in re.split(r'\s+', lines[1].split(':')[1].strip())]
    races = zip(times, distances)

    answer = 1
    for race in races:
        t, d = race
        possible_win = 0
        for i in range(1, t):
            dist = get_distance(i, t-i)
            if dist > d:
                possible_win += 1
        answer *= possible_win

    return answer


def part2(lines):
    t = eval(re.sub(r'\s', '', lines[0].split(':')[1]))
    d = eval(re.sub(r'\s', '', lines[1].split(':')[1]))

    possible_win = 0
    for i in range(1, t):
        dist = get_distance(i, t-i)
        if dist > d:
            possible_win += 1

    return possible_win


def get_distance(speed, time_remaining):
    return speed * time_remaining


if __name__ == '__main__':
    main()
