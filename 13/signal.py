from util import christmas_input

INPUT = [[eval(j) for j in i] for i in christmas_input.file_to_subarray('input.txt')]
TEST_INPUT = [[eval(j) for j in i] for i in christmas_input.file_to_subarray('test_input.txt')]


def check_order(left, right):
    print("  ", left, right)
    if type(left) == list and type(right) == list:
        search_pair = (left, right)
    elif type(left) == list and type(right) == int:
        search_pair = (left, [right])
    elif type(left) == int and type(right) == list:
        search_pair = ([left], right)
    else:
        if left == right:   # No decision possible
            return None
        print("      ", left < right)
        return left < right
    # Recursion
    left_list, right_list = search_pair
    for i in range(min(len(left_list), len(right_list))):
        result = check_order(left_list[i], right_list[i])
        print("            results", result)
        if result is not None:
            return result

    print("          ", search_pair)
    if len(left_list) == len(right_list):  # Right side ran out
        return None
    else:
        return len(left_list) < len(right_list)


def verification_value(data):
    correct_indices = []
    for i, pair in enumerate(data):
        print("PAIR ", i + 1,"\n")
        a, b = pair[0], pair[1]
        if check_order(a, b) is not False:  # Can be none for a non-determination
            correct_indices.append(i + 1)
            print(correct_indices)
    print("Correct", correct_indices, sum(correct_indices))
    return sum(correct_indices)


# assert(verification_value([[[[5, 5], 1], [[5], 5]]]) == 0)
assert verification_value(TEST_INPUT) == 13
print("Part One: ", verification_value(INPUT))