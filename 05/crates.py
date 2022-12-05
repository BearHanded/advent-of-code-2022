from util import christmas_input
import re

TEST_INPUT = christmas_input.file_to_subarray('test_input.txt')
INPUT = christmas_input.file_to_subarray('input.txt')


def parse(arr_input):
    towers = [[] for _ in arr_input[0][0][1:: 4]]
    for row in arr_input[0][-2:: -1]:
        for i, char in enumerate(row[1:: 4]):
            if char != " ":
                towers[i].append(char)
    orders = [[int(s) for s in re.findall(r'-?\d+\.?\d*', move)] for move in arr_input[1]]
    return towers, orders


def execute_orders(towers, orders, move_multiple=False):
    for instruction in orders:  # [count, from, to]
        if move_multiple:  # Part 2
            towers[instruction[2] - 1] += towers[instruction[1] - 1][-1*instruction[0]:]
            del towers[instruction[1] - 1][-1*instruction[0]:]
        else:  # Part 1
            for _ in range(instruction[0]):
                towers[instruction[2] - 1].append(towers[instruction[1] - 1].pop())
    return towers


def run_orders(arr_input, move_multiple=False):
    towers, orders = parse(arr_input)
    towers = execute_orders(towers, orders, move_multiple)
    return ''.join([i[-1] for i in towers])


assert run_orders(TEST_INPUT) == 'CMZ'
assert run_orders(TEST_INPUT, True) == 'MCD'
print("Part One: ", run_orders(INPUT))
print("Part Two: ", run_orders(INPUT, True))
