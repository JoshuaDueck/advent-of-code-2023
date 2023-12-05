import sys
import re

TEST1_ANSWER = 13
TEST2_ANSWER = 30


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

    for card in lines:
        card_array = card.split(': ')[1].split(' | ')
        winning_list = get_num_list(card_array[0])
        have_list = get_num_list(card_array[1])

        score = get_num_winning(winning_list, have_list)
        if score != 0:
            answer += pow(2, score-1)

    return answer


def part2(lines):
    score_list = []

    for card in lines:
        card_array = card.split(': ')[1].split(' | ')
        winning_list = get_num_list(card_array[0])
        have_list = get_num_list(card_array[1])

        score_list.append(get_num_winning(winning_list, have_list))

    num_cards = [1]*len(score_list)
    for i, score in enumerate(score_list):
        for j in range(1, score+1):
            num_cards[i+j] += num_cards[i]

    return sum(num_cards)


def get_num_winning(wl, hl):
    sum = 0
    for val in hl:
        if val in wl:
            sum += 1
    return sum


def get_num_list(s):
    return [eval(i) for i in re.sub(r'\s+', ',', s.strip()).split(',')]


if __name__ == '__main__':
    main()
