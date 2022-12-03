from util import christmas_input

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')


def find_duplicate(contents):
    half = len(contents) // 2
    compartments = [set(contents[:half]), set(contents[half:])]
    return list(compartments[0] & compartments[1]).pop()


def get_priority(character):
    offset = 96
    if character.isupper():
        offset = 38
    return ord(character) - offset


def sum_bags(bags):
    total = 0
    for bag in bags:
        total = total + get_priority(find_duplicate(bag))
    return total


assert sum_bags(TEST_INPUT) == 157
print("Part One: ", sum_bags(INPUT))
