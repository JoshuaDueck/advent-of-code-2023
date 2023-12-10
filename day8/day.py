import sys
from math import lcm

TEST1_ANSWER = 6
TEST2_ANSWER = 6


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
    lines = lines.copy()
    directions = lines.pop(0).strip()

    map = {}

    for line in lines:
        if line != '\n':
            split_line = line.split(' = ')
            map[split_line[0]] = (
                    split_line[1].split(', ')[0][1:],
                    split_line[1].split(', ')[1][:-2]
                )

    prev_node = ''
    curr_node = 'AAA'
    num_steps = 0
    i = 0
    while curr_node != 'ZZZ':
        num_steps += 1
        prev_node = curr_node
        curr_node = map[curr_node][1] if directions[i % len(directions)] == 'R' else map[curr_node][0]
        i += 1

        if prev_node == curr_node:
            print("Infinite loop detected!")
            break
    return num_steps


def part2(lines):
    lines = lines.copy()
    directions = lines.pop(0).strip()

    map = {}

    for line in lines:
        if line != '\n':
            split_line = line.split(' = ')
            map[split_line[0]] = (
                    split_line[1].split(', ')[0][1:],
                    split_line[1].split(', ')[1][:-2]
                )

    start_nodes = []
    end_nodes = []
    for key in map:
        if key[-1] == 'A':
            start_nodes.append(key)
        elif key[-1] == 'Z':
            end_nodes.append(key)

    # Instead, for each start node, determine the shortest path to a Z node
    # Then calculate the LCM for all the start nodes.
    all_steps = []
    for starting_node in start_nodes:
        curr_node = starting_node
        num_steps = 0
        i = 0
        while curr_node not in end_nodes:
            print(curr_node)
            num_steps += 1

            curr_node = map[curr_node][1] if directions[i] == 'R' else map[curr_node][0]

            i += 1
            i %= len(directions)
        all_steps.append(num_steps)

    num_steps = lcm(*all_steps)

    return num_steps


def all_ending_nodes(node_list):
    for node in node_list:
        if node[-1] != 'Z':
            return False
    return True


if __name__ == '__main__':
    main()
