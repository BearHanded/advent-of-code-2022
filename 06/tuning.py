from util import christmas_input

INPUT = christmas_input.file_as_string('input.txt')


def get_marker(signal, char_count=4):
    for i in range(len(signal) - char_count):
        buffer = signal[i:char_count+i]
        if len(set(buffer)) == len(buffer):
            return i + char_count


assert get_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
assert get_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4) == 5
assert get_marker('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert get_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert get_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11

assert get_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert get_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
assert get_marker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert get_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert get_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
print("Part One: ", get_marker(INPUT, 4))
print("Part Two: ", get_marker(INPUT, 14))
