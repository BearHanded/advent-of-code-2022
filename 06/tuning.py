from util import christmas_input

INPUT = christmas_input.file_as_string('input.txt')


def get_marker(signal, char_count=4):
    buffer = [i for i in signal[:char_count]]
    queue = [i for i in signal[char_count:]]
    index = char_count

    if len(set(buffer)) == len(buffer):
        return index

    for char in queue:
        index += 1
        buffer = buffer[1:]
        buffer.append(char)

        if len(set(buffer)) == len(buffer):
            return index


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
print("Part One: ", get_marker(INPUT, 14))
