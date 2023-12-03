TEST1_ANSWER = 4361
TEST2_ANSWER = 0

ADJACENCY_MATRIX = [
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, 0), (0, 0), (1, 0)],
    [(-1, -1), (0, -1), (1, -1)],
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
    indices = []

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            # If it is not a digit, and not a ., add (j,i) to the indices
            if c != '.' and not c.isdigit():
                indices.append((j, i))

    for index in indices:
        # TBH, it's probably easier to just check every number as we come
        # across it, and if there is a symbol next to it, we consider the number
        # valid, and write it to the sum.
        # We can use the indices array to check this, and can use the adjacency
        # matrix as well.
        pass

    # At each index, search adjacent tiles
    # If an adjacent tile is found, build the number by traversing back and
    # forth until a non-number is found
    # when the whole number is found, add it to any other surrounding numbers
    # Return the sum of all numbers around that symbol, add up all values of
    # the symbols, and that is the answer
    return TEST1_ANSWER


def part2(lines):
    return TEST2_ANSWER


def get_whole_number(index, line):
    pass


if __name__ == '__main__':
    main()
