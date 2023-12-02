TEST1_ANSWER = 8
TEST2_ANSWER = 2286


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
    answer = []

    for game in lines:
        # Game 1: x blue, y red, z green; m blue, n red
        game_attempts = game.split(': ')[1].split('; ')
        # ['x blue, y red, z green', 'm blue, n red']

        game_valid = True
        for cubes_drawn in game_attempts:
            # ['x blue, y red, z green']
            set_valid = process_set(cubes_drawn, (12, 13, 14))

            if not set_valid:
                game_valid = False
                break

        answer += [game_valid]

    return get_possible_index_sum(answer)


def part2(lines):
    answer = 0

    for game in lines:
        # Game 1: x blue, y red, z green; m blue, n red
        game_attempts = game.split(': ')[1].split('; ')
        # ['x blue, y red, z green', 'm blue, n red']

        max_r = 0
        max_g = 0
        max_b = 0
        for block_draw in ', '.join(game_attempts).split(', '):
            # 'x blue, y red, z green, m blue, n red'
            block_spl = block_draw.split(' ')
            amnt = int(block_spl[0])
            color = block_spl[1]

            if 'red' in color and amnt > max_r:
                max_r = amnt
            elif 'green' in color and amnt > max_g:
                max_g = amnt
            elif 'blue' in color and amnt > max_b:
                max_b = amnt

        answer += max_r * max_g * max_b

    return answer


def process_set(c_set, bounds):
    split_set = c_set.split(', ')

    for c_set in split_set:
        amnt = int(c_set.split(' ')[0])
        if 'red' in c_set and amnt > bounds[0]:
            return False
        elif 'green' in c_set and amnt > bounds[1]:
            return False
        elif 'blue' in c_set and amnt > bounds[2]:
            return False
    return True


def get_possible_index_sum(ans):
    sum = 0
    for i, val in enumerate(ans):
        if val:
            sum += (i+1)
    return sum


if __name__ == '__main__':
    main()
