from util import christmas_input

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')


def total_overlap(pair):
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (
            pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1])


def partial_overlap(pair):
    return pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]


def sum_overlaps(orders, total_overlap_only=True):
    overlaps = 0
    calc_overlap = total_overlap if total_overlap_only else partial_overlap
    for order in orders:
        pair = [[int(i) for i in elf.split("-")] for elf in order.split(",")]
        if calc_overlap(pair):
            overlaps += 1
    return overlaps


assert sum_overlaps(TEST_INPUT) == 2
assert sum_overlaps(TEST_INPUT, False) == 4

print("Part One: ", sum_overlaps(INPUT))
print("Part Two: ", sum_overlaps(INPUT, False))
