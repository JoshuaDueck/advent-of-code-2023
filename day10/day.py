import sys

TEST1_ANSWER = 0
TEST2_ANSWER = 0


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, 1)
DOWN = (0, -1)


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
    answer = 0
    # Read the lines into a MDA
    # Find the index of S in the MDA
    # Have a moving pair (x, y) that determine current moving directions
    # (horizontally, vertically) traverse, changing only when encountering
    # an L J 7 or F.

    # If move direction is (1, 0), when we traverse, we move right 1.
    # ----> If we encounter a J, we change to (0, 1)
    # ----> If we encounter a 7, we change to (0, -1)
    # If move direction is (0, -1), when we traverse, we move down 1.
    # ----> If we encounter a L, we change to (1, 0)
    # ----> If we encounter a J, we change to (-1, 0)
    # If move direction is (-1, 0), when we traverse, we move left 1.
    # ----> If we encounter a L, we change to (0, 1)
    # ----> If we encounter a F, we change to (0, -1)
    # If move direction is (0, 1), when we traverse, we move up 1.
    # ----> If we encounter a 7, we change to (-1, 0)
    # ----> If we encounter a F, we change to (1, 0)

    # start at S tile (sx,sy) -- find
    # determine start direction by looking at the 4 adjacent tiles
    # If top is 7 or F, start direction is (0, 1)
    # if bottom is J or L, start direction is (0, -1)
    # if left is L or F, start direction is (-1, 0)
    # if right is 7 or J, start direction is (1, 0)
    # Choose the first that makes sense

    """
    num_visited = 1
    curr_tile = find_start() -- this is a tuple containing the char and the
                                coordinates (S, (sx, sy))
    curr_dir = find_start_dir()
    curr_tile = traverse(curr_tile, curr_dir) -- curr_dir is already set and
                                                 correct for this tile, so we
                                                 traverse
    while curr_tile != (S, (sx, sy)):
        num_visited += 1
        if curr_tile[0] == 'L':
            if curr_dir == LEFT:
                curr_dir = UP
            elif curr_dir == DOWN:
                curr_dir = RIGHT
        elif curr_tile[0] == 'J':
            if curr_dir == RIGHT:
                curr_dir = UP
            elif curr_dir == DOWN:
                curr_dir = LEFT
        elif curr_tile[0] == '7':
            if curr_dir == RIGHT:
                curr_dir = DOWN
            elif curr_dir == UP:
                curr_dir = LEFT
        elif curr_tile[0] == 'F':
            if curr_dir == LEFT:
                curr_dir = DOWN
            elif curr_dir == UP:
                curr_dir = RIGHT

        curr_tile = traverse(tiles, curr_tile, curr_dir)

    def traverse(tiles, tile, direction):
        new_coords = (tile[1][0] + direction[0], tile[1][1] + direction[1])
        # The X and Y coords are gonna need to be flipped at some point.
        return (tiles[new_coords[0]][new_coords[1]], new_coords)
    """
    return answer


def part2(lines):
    return TEST2_ANSWER


if __name__ == '__main__':
    main()
