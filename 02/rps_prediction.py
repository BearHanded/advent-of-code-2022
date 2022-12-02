from util import christmas_input
from itertools import groupby

TEST_INPUT = christmas_input.file_to_array('test_input.txt')
INPUT = christmas_input.file_to_array('input.txt')

RESULT_VALUES = {
    "Z": 6,
    "Y": 3,
    "X": 0
}

VICTORY_CONDITIONS = {
    "Y": "A",
    "Z": "B",
    "X": "C"
}

MOVE_VALS = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def rps_calc(guide):
    rounds = [vals.split(" ") for vals in guide]
    totalScore = 0
    for round_data in rounds:
        round_score = RESULT_VALUES[round_data[1]]
        move_offset = (round_score / 3) - 1
        move_val = (MOVE_VALS[round_data[0]] + move_offset) % 3
        if move_val == 0:
            move_val = 3
        totalScore = totalScore + round_score + move_val
    print(totalScore)
    return totalScore


assert rps_calc(TEST_INPUT) == 12
print("Part Two: ", rps_calc(INPUT))
