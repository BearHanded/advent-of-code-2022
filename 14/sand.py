from util import christmas_input

INPUT = 'input.txt'
TEST_INPUT = 'test_input.txt'
SAND_START = (500, 0)


def build_map(filename):
    lines = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in christmas_input.file_to_array(filename)]
    stone_set = set()
    max_y = 0
    for line in lines:
        for i in range(len(line) - 1):
            a = line[i]
            b = line[i + 1]
            magnitude_x = abs(a[0] - b[0])
            magnitude_y = abs(a[1] - b[1])
            x_dir = -1 if (a[0] - b[0]) >= 0 else 1
            y_dir = -1 if (a[1] - b[1]) >= 0 else 1
            for x in range(magnitude_x + 1):
                for y in range(magnitude_y + 1):
                    # Since only horizontal & vert, this is safe
                    point = (a[0] + x * x_dir, a[1] + y * y_dir)
                    stone_set.add(point)
                    if point[1] > max_y:
                        max_y = point[1]
    return stone_set, max_y


def simulate_sand(stone_set, max_y, floor=None):
    settled = False
    x, y = SAND_START
    y_out = max_y
    while not settled and y <= max_y:
        # Keep falling if avail
        if floor and y == (floor - 1):
            settled = True
            stone_set.add((x, y))
            break
        elif (x, y + 1) not in stone_set:
            y += 1
            continue

        # collision, check if side scatter
        if (x - 1, y + 1) not in stone_set:
            x -= 1
            y += 1
            continue
        elif (x + 1, y + 1) not in stone_set:
            x += 1
            y += 1
            continue

        settled = True
        stone_set.add((x, y))
        if y > max_y:
            y_out = max_y if max_y > y else y

    return settled, y_out


def max_moves_void(filename):
    stone_set, max_y = build_map(filename)
    running = True
    total_sand = 0
    while running:
        total_sand += 1
        running, max_y = simulate_sand(stone_set, max_y)
    print(total_sand - 1)
    return total_sand - 1


def max_moves_floor(filename):
    stone_set, max_y = build_map(filename)
    running = True
    total_sand = 0
    max_y += 2
    floor_height = max_y
    while running and SAND_START not in stone_set:
        total_sand += 1
        running, max_y = simulate_sand(stone_set, max_y, floor=floor_height)
    return total_sand


assert max_moves_void(TEST_INPUT) == 24
print("Part One: ", max_moves_void(INPUT))
assert max_moves_floor(TEST_INPUT) == 93
print("Part Two: ", max_moves_floor(INPUT))
