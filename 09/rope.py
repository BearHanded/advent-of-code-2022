from util import christmas_input

INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('input.txt')]
TEST_INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('test_input.txt')]
TEST_INPUT_2 = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('test_input_2.txt')]

DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def total_tail_positions(orders, rope_length=2):
    segments = [[0, 0] for _ in range(rope_length)]
    tail_locations = set()

    for order in orders:
        ray = DIRECTIONS[order[0]]
        for _ in range(int(order[1])):
            segments[0] = [segments[0][0] + ray[0], segments[0][1] + ray[1]]
            for i, current in enumerate(segments[1:]):
                # Note segment[i] is the prior segment, as the iteration starts at +1
                diff_x = segments[i][0] - current[0]
                diff_y = segments[i][1] - current[1]

                if abs(diff_y) > 1:
                    current[1] += (1 if diff_y > 0 else -1)
                    if diff_x != 0:
                        current[0] += (1 if diff_x > 0 else -1)
                elif abs(diff_x) > 1:
                    current[0] += (1 if diff_x > 0 else -1)
                    if diff_y != 0:
                        current[1] += (1 if diff_y > 0 else -1)
                if i == (rope_length - 2):
                    tail_locations.add((current[0], current[1]))
    return len(tail_locations)


assert total_tail_positions(TEST_INPUT) == 13
assert total_tail_positions(TEST_INPUT, 10) == 1
assert total_tail_positions(TEST_INPUT_2, 10) == 36

print("PART ONE: ", total_tail_positions(INPUT))
print("PART ONE: ", total_tail_positions(INPUT, 10))
