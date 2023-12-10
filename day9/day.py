import sys

TEST1_ANSWER = 114
TEST2_ANSWER = 2


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
    for line in lines:
        nums = [eval(i) for i in line.strip().split(' ')]
        answer += gnis(nums)
    return answer


def part2(lines):
    answer = 0
    for line in lines:
        nums = [eval(i) for i in line.strip().split(' ')]
        nums.reverse()
        answer += gnis(nums)
    return answer


def gnis(nums):
    if not all(i == 0 for i in nums):
        gap_list = get_gap_list(nums)
        return nums[-1] + gnis(gap_list)
    else:
        return 0


def get_gap_list(nums):
    gap_list = []
    for i in range(len(nums) - 1):
        gap_list.append(nums[i + 1] - nums[i])
    return gap_list


if __name__ == '__main__':
    main()
