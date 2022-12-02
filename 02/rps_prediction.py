from util import christmas_input

TEST_INPUT = [pair.split(" ") for pair in christmas_input.file_to_array('test_input.txt')]
INPUT = [pair.split(" ") for pair in christmas_input.file_to_array('input.txt')]

RESULT_VALUES = {
    "Z": 6,
    "Y": 3,
    "X": 0
}

MOVE_VALUES = {
    "A": 1,
    "B": 2,
    "C": 3,
}


def rps_calc(guide):
    rounds = [vals.split(" ") for vals in guide]
    totalScore = 0
    for round_data in rounds:
        round_score = RESULT_VALUES[round_data[1]]
        move_offset = (round_score / 3) - 1  # If you know win/loss/tie, you know the player move
        move_score = (MOVE_VALUES[round_data[0]] + move_offset) % 3
        if move_score == 0:
            move_score = 3
        totalScore = totalScore + round_score + move_score
    return totalScore


assert rps_calc(TEST_INPUT) == 12
print("Part Two: ", rps_calc(INPUT))
