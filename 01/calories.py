from util import christmas_input
from itertools import groupby

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')


def top_calories_sum(calories, total_elves=1):
    calorie_groups = [sum(list(int(i) for i in sub)) for ele, sub in groupby(calories, key=bool) if ele]
    calorie_groups.sort(reverse=True)
    top_calories = calorie_groups[0:total_elves]
    return sum(top_calories);


assert top_calories_sum(TEST_INPUT) == 24000
assert top_calories_sum(TEST_INPUT, 3) == 45000

print("Part One: ", top_calories_sum(INPUT))
print("Part Two: ", top_calories_sum(INPUT, 3))
