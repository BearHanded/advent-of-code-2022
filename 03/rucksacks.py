from util import christmas_input

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')


def find_duplicate(contents):
    compartments = [set(i) for i in contents]
    overlap = set.intersection(*compartments)
    return list(overlap).pop()


def get_priority(character):
    offset = 96
    if character.isupper():
        offset = 38
    return ord(character) - offset


# Part One
def sum_bag_priority(bags):
    total = 0
    for bag in bags:
        bag_pivot = len(bag) // 2
        compartments = [set(bag[:bag_pivot]), set(bag[bag_pivot:])]
        total = total + get_priority(find_duplicate(compartments))
    return total


# Part Two
def sum_badges(bags):
    #  Chunk into groups of 3, get intersection
    groups = [bags[i:i + 3] for i in range(0, len(bags), 3)]
    total = 0
    for group in groups:
        total = total + get_priority(find_duplicate(group))
    return total


assert sum_bag_priority(TEST_INPUT) == 157
assert sum_badges(TEST_INPUT) == 70

print("Part One: ", sum_bag_priority(INPUT))
print("Part Two: ", sum_badges(INPUT))
