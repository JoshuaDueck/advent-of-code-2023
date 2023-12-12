import sys
import math

TEST1_ANSWER = 374
TEST2_ANSWER = 8410


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
    galaxy_coords = []
    empty_rows = []
    empty_cols = []

    for y, line in enumerate(lines):
        if all(char == '.' for char in line.strip()):
            empty_rows.append(y)

    for x in range(len(lines[0])):
        if all(line[x] == '.' for line in lines):
            empty_cols.append(x)

    extra_skip_y = 0
    for y, line in enumerate(lines):
        if y in empty_rows:
            extra_skip_y += 1
        extra_skip_x = 0
        for x, char in enumerate(line):
            if x in empty_cols:
                extra_skip_x += 1
            if char == '#':
                galaxy_coords.append((x+extra_skip_x, y+extra_skip_y))

    diffs = []
    answer = 0
    count = 0
    # total_records = nCr(len(galaxy_coords), 2)
    for i, coord in enumerate(galaxy_coords):
        for j in range(i, len(galaxy_coords)):
            coord_2 = galaxy_coords[j]
            # print(f"Calculating {count}/{total_records}")
            if coord != coord_2 and (coord_2, coord) not in diffs:
                count += 1
                answer += abs(coord[0]-coord_2[0]) + abs(coord[1]-coord_2[1])
                diffs.append((coord, coord_2))
                # print(answer)

    return answer


def part2(lines):
    galaxy_coords = []
    empty_rows = []
    empty_cols = []

    for y, line in enumerate(lines):
        if all(char == '.' for char in line.strip()):
            empty_rows.append(y)

    for x in range(len(lines[0])):
        if all(line[x] == '.' for line in lines):
            empty_cols.append(x)

    extra_skip_y = 0
    for y, line in enumerate(lines):
        if y in empty_rows:
            extra_skip_y += 999999
        extra_skip_x = 0
        for x, char in enumerate(line):
            if x in empty_cols:
                extra_skip_x += 999999
            if char == '#':
                galaxy_coords.append((x+extra_skip_x, y+extra_skip_y))

    diffs = []
    answer = 0
    count = 0
    total_records = nCr(len(galaxy_coords), 2)
    for i, coord in enumerate(galaxy_coords):
        for j in range(i, len(galaxy_coords)):
            coord_2 = galaxy_coords[j]
            print(f"Calculating {count}/{total_records}")
            if coord != coord_2 and (coord_2, coord) not in diffs:
                count += 1
                answer += abs(coord[0]-coord_2[0]) + abs(coord[1]-coord_2[1])
                diffs.append((coord, coord_2))

    return answer


def nCr(n, r):
    n_fact = math.factorial(n)
    r_fact = math.factorial(r)
    n_minus_r_fact = math.factorial(n - r)
    result = n_fact // (r_fact * n_minus_r_fact)
    return result


if __name__ == '__main__':
    main()
