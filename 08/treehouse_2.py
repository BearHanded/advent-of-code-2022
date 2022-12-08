from util import christmas_input

INPUT = [[int(i) for i in list(line)] for line in christmas_input.file_to_array('input.txt')]
TEST_INPUT = [[int(i) for i in list(line)] for line in christmas_input.file_to_array('test_input.txt')]


def visible_trees(x_start, y_start, forest, direction, initial_height=-1):
    path = []
    seen = set()
    x = x_start
    y = y_start

    while (0 <= x < len(forest[0])) and (0 <= y < len(forest)):
        target = forest[y][x]
        if initial_height >= 0:
            if initial_height > target:
                seen.add((x, y))
            else:
                seen.add((x, y))
                break
        elif len(path) == 0 or all(target > height for height in path):
            seen.add((x, y))
        path.append(target)
        x += direction[0]
        y += direction[1]
    return seen


def count_trees(forest):
    trees_seen = set()
    for y in range(len(forest)):
        # R/L
        trees_seen.update(visible_trees(0, y, forest, (1, 0)))
        trees_seen.update(visible_trees(len(forest) - 1, y, forest, (-1, 0)))

    for x in range(len(forest[0])):
        # Bottom / Top
        trees_seen.update(visible_trees(x, 0, forest, (0, 1)))
        trees_seen.update(visible_trees(x, len(forest) - 1, forest, (0, -1)))
    return len(trees_seen)


def get_scenic_score(x, y, forest):
    score = 1
    if x == 0 or x == (len(forest[0]) - 1) or y == 0 or y == (len(forest) - 1):
        return 0
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # D, R, L, U
    for direction in dirs:
        look_x = x + direction[0]
        look_y = y + direction[1]
        score_direction = len(visible_trees(look_x, look_y, forest, direction, initial_height=forest[y][x]))
        score *= score_direction
    return score


def high_score(forest):
    highest = 0
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            score = get_scenic_score(x, y, forest)
            if score > highest:
                highest = score
    return highest


assert count_trees(TEST_INPUT) == 21
print("Part One: ", count_trees(INPUT))

assert get_scenic_score(2, 1, TEST_INPUT) == 4
assert get_scenic_score(2, 3, TEST_INPUT) == 8
print("high_score: ", high_score(INPUT))
