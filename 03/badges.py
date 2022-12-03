from util import christmas_input

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')


def get_groups(bags):
    return [bags[i:i + 3] for i in range(0, len(bags), 3)]


def find_badge(bags):
    bag_sets = [set(i) for i in bags]
    return list(bag_sets[0] & bag_sets[1] & bag_sets[2]).pop()


def get_priority(character):
    offset = 96
    if character.isupper():
        offset = 38
    return ord(character) - offset


def sum_badges(bags):
    groups = get_groups(bags)
    total = 0
    for group in groups:
        total = total + get_priority(find_badge(group))
    return total


assert sum_badges(TEST_INPUT) == 70
print("Part Two: ", sum_badges(INPUT))
