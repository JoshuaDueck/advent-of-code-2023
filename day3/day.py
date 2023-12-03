TEST1_ANSWER = 4361
TEST2_ANSWER = 467835

ADJACENCY_MATRIX = [
    (-1, 1), (0, 1), (1, 1),
    (-1, 0), (0, 0), (1, 0),
    (-1, -1), (0, -1), (1, -1),
]


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

    with open('input.txt') as f:
        lines = f.readlines()

        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


def part1(lines):
    # Find indices of any symbol (use a check, if not int, and not '.', symbol)
    indices = set()

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            # If it is not a digit, and not a ., add (j, i) to the indices
            if c != '.' and not c.isdigit() and c != '\n':
                indices.add((x, y))

    answer = 0
    for y, line in enumerate(lines):
        curr_digit_str = ''
        curr_valid = False
        for x, c in enumerate(line):
            if c.isdigit():
                # We are currently in a digit, check surrounding tiles to see
                # if it is next to a symbol index, if so, it is a valid number
                for tile in ADJACENCY_MATRIX:
                    adj_x = x+tile[0]
                    adj_y = y+tile[1]

                    if (adj_x, adj_y) in indices:
                        curr_valid = True
                curr_digit_str += c
            elif c == '.' or c == '\n':
                # The number has ended, either by . or newline, set it if it
                # is valid, then reset
                if curr_valid:
                    answer += int('0'+curr_digit_str)
                curr_digit_str = ''
                curr_valid = False
            else:
                # It is the symbol, so it is valid, but reset anyways
                answer += int('0'+curr_digit_str)
                curr_digit_str = ''
                curr_valid = False

    return answer


def part2(lines):
    # Find indices of any symbol (use a check, if not int, and not '.', symbol)
    gear_candidates = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            # If the character is a *, we have a gear candidate
            if c == '*':
                # Initialize the gear candidate number list
                gear_candidates[(x, y)] = []

    # Check all numbers, if it is next to a gear candidate, set it as valid
    # After the number has been validated (store is_valid as a gear candidate
    # index), add it to that index's list, and continue
    for y, line in enumerate(lines):
        curr_digit_str = ''
        valid_gc = None
        for x, c in enumerate(line):
            if c.isdigit():
                # c is a digit, check surroundings for gear candidate
                for tile in ADJACENCY_MATRIX:
                    adj_x = x+tile[0]
                    adj_y = y+tile[1]

                    if (adj_x, adj_y) in gear_candidates:
                        valid_gc = (adj_x, adj_y)
                curr_digit_str += c
            elif c == '.' or c == '\n' and c != '*':
                # The number has ended, either by ., newline, or other
                # character than *
                if valid_gc is not None and curr_digit_str != '':
                    gear_candidates[valid_gc].append(int(curr_digit_str))
                curr_digit_str = ''
                valid_gc = None
            elif c == '*' and curr_digit_str != '':
                valid_gc = (x, y)
                gear_candidates[valid_gc].append(int(curr_digit_str))
                curr_digit_str = ''
                valid_gc = None

    answer = 0

    for can in gear_candidates:
        can_values = gear_candidates[can]
        if len(can_values) == 2:
            answer += can_values[0] * can_values[1]

    return answer


if __name__ == '__main__':
    main()
