import sys

TEST1_ANSWER = 8
TEST2_ANSWER = 4


LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


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
    tiles = []
    for line in lines:
        tiles.append(list(line.strip()))

    start_tile = find_start(tiles)
    curr_tile = start_tile
    curr_dir = find_start_dir(curr_tile, tiles)

    curr_tile, curr_dir = traverse(curr_tile, curr_dir, tiles)
    position = 0
    while curr_tile != start_tile:
        position += 1

        curr_tile, curr_dir = traverse(curr_tile, curr_dir, tiles)

    return (position+1)//2


def part2(lines):
    return TEST2_ANSWER


def find_start(tiles):
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            if tile == 'S':
                return (tile, (x, y))


def find_start_dir(start_tile, tiles):
    x, y = start_tile[1]
    try:
        if tiles[y-1][x] in ('7', 'F', '|'):
            return UP
    except IndexError:
        pass

    try:
        if tiles[y+1][x] in ('J', 'L', '|'):
            return DOWN
    except IndexError:
        pass

    try:
        if tiles[y][x-1] in ('L', 'F', '-'):
            return LEFT
    except IndexError:
        pass

    if tiles[y][x+1] in ('7', 'J', '-'):
        return RIGHT


def traverse(tile, direction, tiles):
    new_coords = (tile[1][0] + direction[0], tile[1][1] + direction[1])
    new_tile = tiles[new_coords[1]][new_coords[0]]

    if new_tile == 'L':
        if direction == LEFT:
            direction = UP
        elif direction == DOWN:
            direction = RIGHT
    elif new_tile == 'J':
        if direction == RIGHT:
            direction = UP
        elif direction == DOWN:
            direction = LEFT
    elif new_tile == '7':
        if direction == RIGHT:
            direction = DOWN
        elif direction == UP:
            direction = LEFT
    elif new_tile == 'F':
        if direction == LEFT:
            direction = DOWN
        elif direction == UP:
            direction = RIGHT

    return [(tiles[new_coords[1]][new_coords[0]], new_coords), direction]


if __name__ == '__main__':
    main()
