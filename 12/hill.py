from util import christmas_input

INPUT = christmas_input.file_to_array('input.txt')
TEST_INPUT = christmas_input.file_to_array('test_input.txt')


def build_map(raw):
    landscape = [i.split("") for i in raw]
    for i in range(len(landscape)):
        for j in range(len(landscape[i])):
            if landscape[i][j] == "S":
                start = (j,i)
            elif landscape[i][j] == "E":
                end = (j,i)
    return landscape, start, end

def adjacent(x, y, max_x, max_y):
    adj = []
    for pair in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = pair[0] + x
        next_y = pair[1] + y
        if 0 <= next_x < max_x and 0 <= next_y < max_y:
            adj.append((next_x, next_y))
    return adj


def traverse(raw):
    landscape, start, end = build_map(raw)
    max_y = len(landscape)
    max_x = len(landscape[0])
    costs = {start: 0}
    explore_queue = [start]

    for (x, y) in explore_queue:
        for (x1, y1) in adjacent(x, y, max_x, max_y):
            # Save to known values
            if (x1, y1) in costs and costs[x1, y1] <= costs[x, y] + hill[y1][x1]:
                continue
            costs[x1, y1] = costs[x, y] + cavern[y1][x1]  # running total, min to get to a given point
            explore_queue.append((x1, y1))
    print("Min journey:", costs[end])





assert traverse(TEST_INPUT) == 31
print("Part One: ", traverse(INPUT))
