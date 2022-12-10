from util import christmas_input

INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('input.txt')]
TEST_INPUT = [[i for i in line.split(" ")] for line in christmas_input.file_to_array('test_input.txt')]

CYCLE_TIMING = {
    "noop": 1,
    "addx": 2
}


def pretty_display(pixels):
    print("================================================================================")
    for row in pixels:
        print(' '.join(row))
    print("================================================================================")


def signal_strength(commands):
    cycle = 0
    signal_str = 0
    x = 1
    out = [[], [], [], [], [], []]
    out_row = 0

    for executing_op in commands:
        for _ in range(CYCLE_TIMING[executing_op[0]]):
            cycle += 1
            # Signal Strength
            if cycle == 20 or (cycle - 20) % 40 == 0:
                signal_str += cycle * x

            # Print logic
            pixel = "#" if x - 1 <= len(out[out_row]) <= x + 1 else " "
            out[out_row].append(pixel)
            if cycle % 40 == 0:
                out_row += 1

        if executing_op[0] == "addx":
            x += int(executing_op[1])
    pretty_display(out)
    return signal_str


assert signal_strength(TEST_INPUT) == 13140
print("Part One: ", signal_strength(INPUT))
