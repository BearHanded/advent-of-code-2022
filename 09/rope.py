from util import christmas_input

INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('input.txt')]
TEST_INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('test_input.txt')]

DIRECTIONS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}


def total_tail_positions(orders):
    head = (0, 0)
    tail = [0, 0]
    tail_locations = set()

    for orders in orders:
        ray = DIRECTIONS[orders[0]]
        for _ in range(int(orders[1])):
            head = (head[0] + ray[0], head[1] + ray[1])
            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]
            if abs(diff_x) > 1:
                tail[0] += 1 if diff_x > 0 else -1
                if head[1] != tail[1]:
                    tail[1] = head[1]
            elif abs(diff_y) > 1:
                tail[1] += 1 if diff_y > 0 else -1
                if head[0] != tail[0]:
                    tail[0] = head[0]

            tail_locations.add((tail[0],tail[1]))
            print(head, "-", tail)
    print(len(tail_locations), tail_locations)
    return len(tail_locations)


assert total_tail_positions(TEST_INPUT) == 13
print("PART ONE: ", total_tail_positions(INPUT))
