TEST1_ANSWER = 142
TEST2_ANSWER = 281


# This is kind of a dirty trick, but because some early numbers replace
# later numbers, there's no way of ensuring earlier bigger numbers are not
# broken by replacing a smaller but later overlapping number
# (eightwone => eightw1). This way, it becomes (eightwo2twone1one), so two can
# be replaced after one, and eight after two, and the order is preserved.
DIGITS = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine',
    'zero': 'zero0zero',
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
            return

    with open('testinput2.txt') as f:
        lines = f.readlines()
        result = part2(lines)
        if result == TEST2_ANSWER:
            print("Test passed, continuing...")
        else:
            print("Test failed, \
                    expected: {}, actual: {}".format(TEST2_ANSWER, result))
            return

    with open('input.txt') as f:
        lines = f.readlines()

        print("Part 1:", part1(lines))
        print("Part 2:", part2(lines))


def part1(lines):
    answer = 0
    for line in lines:
        answer += get_line_value(line)

    return answer


# Main strategy is to replace all instances of digits in the line, then
# run part 1's solution as before and it should work fine.
def part2(lines):
    answer = 0
    for line in lines:
        answer += get_line_value(numify_line(line))
    return answer


# If character is a digit, and first digit has not been set, set it.
# Then set the last digit, which by the end of the string will be correct.
# Add them up as a 2 digit number, and that's the line's value.
# Would break on a single-digit number, but the puzzle said it would be a
# 2-digit number, so this works perfectly.
def get_line_value(line):
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = int(char)
            last_digit = int(char)
    return first_digit * 10 + last_digit


def numify_line(line):
    clean_line = line
    for key in DIGITS:
        clean_line = clean_line.replace(key, DIGITS[key])
    return clean_line


if __name__ == '__main__':
    main()
