from collections import defaultdict

from util import christmas_input

INPUT = christmas_input.file_to_array('input.txt')
TEST_INPUT = christmas_input.file_to_array('test_input.txt')

THRESHOLD = 100000


def build_dir_map(output):
    cursor = ["/"]
    dir_map = defaultdict(int)
    for line in output:
        parts = line.split(" ")
        if parts[0] == "$":  # $ cd a / $ cd ..
            if parts[1] == "cd":
                if parts[2] == "/":
                    cursor = ["/"]
                elif parts[2] == "..":
                    cursor.pop()
                else:
                    cursor.append(parts[2])
            elif parts[1] == "ls":
                continue  # don't care atm
        elif parts[0] != "dir":
            for i in range(len(cursor)):
                idx = tuple(cursor[:i + 1])
                # print(idx)
                dir_map[idx] += int(parts[0])
    return dir_map


def get_file_metrics(output):
    dir_map = build_dir_map(output)
    deletable = sum(size for size in dir_map.values() if size <= THRESHOLD)
    unused = 30000000 - (70000000 - dir_map[tuple("/")])
    minimum = min(dir_map[path] for path in dir_map if unused <= dir_map[path])
    return deletable, minimum


assert get_file_metrics(TEST_INPUT) == (95437, 24933642)
print("Deletable/Min increase: ", get_file_metrics(INPUT))
