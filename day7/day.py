import sys
import re

TEST1_ANSWER = 6440
TEST2_ANSWER = 5905

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

HAND_LABELS = [
    'High Card',
    'One Pair',
    'Two Pairs',
    'Three of a Kind',
    'Full House',
    'Four of a Kind',
    'Five of a Kind'
]


CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

CARD_VALUES_2 = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}


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
    ordered_hands = []

    for line in lines:
        split_line = line.split(' ')
        ordered_hands.append((split_line[0], int(split_line[1])))

    by_hand_type = {}

    for hand in ordered_hands:
        if get_hand_value(hand[0]) not in by_hand_type:
            by_hand_type[get_hand_value(hand[0])] = [hand]
        else:
            by_hand_type[get_hand_value(hand[0])].append(hand)

    for hand_type in by_hand_type:
        for i in range(0, 5):
            by_hand_type[hand_type] = sorted(
                by_hand_type[hand_type],
                key=lambda hand: hand_to_num(hand[0]),
            )

    ordered_hands = []
    for hand_type in sorted(by_hand_type):
        ordered_hands += by_hand_type[hand_type]

    answer = 0

    for i, hand in enumerate(ordered_hands):
        answer += hand[1]*(i+1)

    return answer


def part2(lines):
    # 250146490 is too low
    ordered_hands = []

    for line in lines:
        split_line = line.split(' ')
        ordered_hands.append((split_line[0], int(split_line[1])))

    by_hand_type = {}

    for hand in ordered_hands:
        if get_hand_value_pt2(hand[0]) not in by_hand_type:
            by_hand_type[get_hand_value_pt2(hand[0])] = [hand]
        else:
            by_hand_type[get_hand_value_pt2(hand[0])].append(hand)

    for hand_type in by_hand_type:
        for i in range(0, 5):
            by_hand_type[hand_type] = sorted(
                by_hand_type[hand_type],
                key=lambda hand: hand_to_num_pt2(hand[0]),
            )

    ordered_hands = []
    for hand_type in sorted(by_hand_type):
        ordered_hands += by_hand_type[hand_type]

    answer = 0

    for i, hand in enumerate(ordered_hands):
        answer += hand[1]*(i+1)

    return answer


def get_hand_value(cards):
    card_set = set(cards)
    if len(card_set) == 1:
        # 5 of a kind
        return FIVE_OF_A_KIND
    elif len(card_set) == 2:
        # 4 of a kind or full house
        card_dict = {}
        for card in cards:
            if card not in card_dict:
                card_dict[card] = 1
            else:
                card_dict[card] += 1

        for card in card_dict:
            if card_dict[card] == 4:
                return FOUR_OF_A_KIND
        return FULL_HOUSE
    elif len(card_set) == 3:
        # 3 of a kind or 2 pair
        card_dict = {}
        for card in cards:
            if card not in card_dict:
                card_dict[card] = 1
            else:
                card_dict[card] += 1

        for card in card_dict:
            if card_dict[card] == 3:
                return THREE_OF_A_KIND
        return TWO_PAIR
    elif len(card_set) == 4:
        # 1 pair
        return ONE_PAIR
    elif len(card_set) == 5:
        # High card
        return HIGH_CARD


def get_hand_value_pt2(cards):
    cards = best_joker_hand(cards)
    card_set = set(cards)
    if len(card_set) == 1:
        # 5 of a kind
        return FIVE_OF_A_KIND
    elif len(card_set) == 2:
        # 4 of a kind or full house
        card_dict = {}
        for card in cards:
            if card not in card_dict:
                card_dict[card] = 1
            else:
                card_dict[card] += 1

        for card in card_dict:
            if card_dict[card] == 4:
                return FOUR_OF_A_KIND
        return FULL_HOUSE
    elif len(card_set) == 3:
        # 3 of a kind or 2 pair
        card_dict = {}
        for card in cards:
            if card not in card_dict:
                card_dict[card] = 1
            else:
                card_dict[card] += 1

        for card in card_dict:
            if card_dict[card] == 3:
                return THREE_OF_A_KIND
        return TWO_PAIR
    elif len(card_set) == 4:
        # 1 pair
        return ONE_PAIR
    elif len(card_set) == 5:
        # High card
        return HIGH_CARD


def card_place_value(hand, index):
    return CARD_VALUES[hand[index]]


def card_place_value_pt2(hand, index):
    return CARD_VALUES_2[hand[index]]


def hand_to_num(hand):
    new_hand = ''
    for i in range(0, 5):
        new_hand += str(card_place_value(hand, i)).zfill(3)
    return int(new_hand)


def hand_to_num_pt2(hand):
    new_hand = ''
    for i in range(0, 5):
        new_hand += str(card_place_value_pt2(hand, i)).zfill(3)
    return int(new_hand)


def best_joker_hand(hand):
    if hand == 'JJJJJ':
        return 'KKKKK'
    most_common_card = hand[0]
    most_common_card_count = 1
    for card in hand:
        if card != 'J' and hand.count(card) >= most_common_card_count:
            most_common_card = card
            most_common_card_count = hand.count(card)

    return re.sub('J', most_common_card, hand)


if __name__ == '__main__':
    main()
