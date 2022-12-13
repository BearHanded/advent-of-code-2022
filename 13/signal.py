from util import christmas_input
from functools import cmp_to_key

INPUT = [[eval(j) for j in i] for i in christmas_input.file_to_subarray('input.txt')]
TEST_INPUT = [[eval(j) for j in i] for i in christmas_input.file_to_subarray('test_input.txt')]


def check_order(left, right):
    if type(left) == list and type(right) == list:
        search_pair = (left, right)
    elif type(left) == list and type(right) == int:
        search_pair = (left, [right])
    elif type(left) == int and type(right) == list:
        search_pair = ([left], right)
    else:
        if left == right:   # No decision possible
            return 0
        return 1 if left < right else -1
    # Recursion
    left_list, right_list = search_pair
    for i in range(min(len(left_list), len(right_list))):
        result = check_order(left_list[i], right_list[i])
        if result is not 0:
            return result

    if len(left_list) == len(right_list):  # Right side ran out
        return 0
    else:
        return 1 if len(left_list) < len(right_list) else -1


def verification_value(data):
    correct_indices = []
    for i, pair in enumerate(data):
        a, b = pair[0], pair[1]
        if check_order(a, b) >= 0:  # Can be none for a non-determination
            correct_indices.append(i + 1)
    return sum(correct_indices)


def decoder_key(f):
    signals = [eval(i) for i in christmas_input.file_to_array(f) if i]
    markers = [[[2]], [[6]]]
    signals.extend(markers)
    signals.sort(key=cmp_to_key(check_order))
    signals.reverse()  # backwards because of -1 vs 1, oops

    key = 1
    for i, signal in enumerate(signals):
        if signal in markers:
            key *= i + 1
    return key


assert verification_value(TEST_INPUT) == 13
print("Part One: ", verification_value(INPUT))
assert decoder_key("test_input.txt") == 140
print("Part TWO: ", decoder_key("input.txt"))