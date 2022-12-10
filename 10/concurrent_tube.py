from util import christmas_input

# This was a mistake and overcomplicated the prompt.
# Saving just in case we do need concurrent instructions in the future
INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('input.txt')]
TEST_INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('test_input.txt')]

CYCLE_TIMING = {
    "noop": 0,
    "addx": 1
}


def queue_insert(queue, position, value):
    size = len(queue)
    if len(queue) < position + 1:
        queue.extend([] for _ in range(size, position + 1))
    queue[position].append(value)


def signal_strength(commands):
    cycle = 1
    signal_str = 0
    queue = []
    x = 1
    while len(queue) > 0 or cycle <= len(commands):
        # Set queue
        if cycle <= len(commands):
            op = commands[cycle - 1]
            queue_insert(queue, CYCLE_TIMING[op[0]], op)

        # Process
        current_ops = queue.pop(0);
        for executing_op in current_ops:
            # if executing_op[0] == "noop":
            if executing_op[0] == "addx":
                x += int(executing_op[1])
        if cycle == 20 or (cycle - 20) % 40 == 0:
            signal_str += cycle * x
            print("  ", cycle, x)
            print("SIGNAL STR -", cycle, signal_str)
        cycle += 1
    return signal_str


assert signal_strength(TEST_INPUT) == 13140
print("Part One: ", signal_strength(INPUT))
