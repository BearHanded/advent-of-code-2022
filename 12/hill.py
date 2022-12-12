from util import christmas_input

INPUT = christmas_input.file_to_array('input.txt')
TEST_INPUT = christmas_input.file_to_array('test_input.txt')


def build_map(raw):
    landscape = [list(i) for i in raw]
    start = ()
    end = ()
    for i in range(len(landscape)):
        for j in range(len(landscape[i])):
            if landscape[i][j] == "S":
                start = (j, i)
                landscape[i][j] = "a"
            elif landscape[i][j] == "E":
                end = (j, i)
                landscape[i][j] = "z"
    return landscape, start, end


def adjacent(x, y, max_x, max_y, landscape):
    adj = []
    for pair in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        next_x = pair[0] + x
        next_y = pair[1] + y
        if 0 <= next_x < max_x and 0 <= next_y < max_y:  # In Range
            if ord(landscape[next_y][next_x]) - ord(landscape[y][x]) <= 1:
                adj.append((next_x, next_y))
    return adj


def traverse(landscape, start, end):
    max_y = len(landscape)
    max_x = len(landscape[0])
    costs = {start: (0, [start])}
    explore_queue = [start]

    for (x, y) in explore_queue:
        for (x1, y1) in adjacent(x, y, max_x, max_y, landscape):
            # Save to known values
            if (x1, y1) in costs and costs[x1, y1][0] <= costs[x, y][0] + 1:
                continue
            costs[x1, y1] = (costs[x, y][0] + 1, costs[x, y][1].copy())  # running total, min to get to a given point
            costs[x1, y1][1].append((x1,y1))
            explore_queue.append((x1, y1))

    if end not in costs:
        return -1
    # test = []
    # for x_test, y_test in costs[end][1]:
    #     test.append(landscape[y_test][x_test])
    # print("Path Taken: ", test)
    return costs[end][0]


def climb(raw):
    landscape, start, end = build_map(raw)
    return traverse(landscape, start, end)


def best_climb(raw):
    landscape, _, end = build_map(raw)
    start_candidates = []
    best = 100000000000000
    for i in range(len(landscape)):
        for j in range(len(landscape[i])):
            if landscape[i][j] == "a":
                start_candidates.append((j, i))
    for candidate in start_candidates:
        potential_path = traverse(landscape, candidate, end)
        if 0 < potential_path < best:
            best = potential_path
    print(best)
    return best


assert climb(TEST_INPUT) == 31
print("Part One: ", climb(INPUT))
assert best_climb(TEST_INPUT) == 29
print("Part One: ", best_climb(INPUT))