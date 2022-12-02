from util import christmas_input

TEST_INPUT = [pair.split(" ") for pair in christmas_input.file_to_array('test_input.txt')]
INPUT = [pair.split(" ") for pair in christmas_input.file_to_array('input.txt')]


RESULT_VALUES = {
    "WIN": 6,
    "DRAW": 3,
    "LOSS": 0
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
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def rps_score(rounds):
    totalScore = 0
    for round_moves in rounds:
        totalScore = totalScore + score(round_moves[0], round_moves[1])
    return totalScore


def score(opponent, player):
    result = 0
    if MOVE_VALS[player] == MOVE_VALS[opponent]:
        result = RESULT_VALUES["DRAW"]
    elif VICTORY_CONDITIONS[player] == opponent:
        result = RESULT_VALUES["WIN"]
    return result + MOVE_VALS[player]


assert rps_score(TEST_INPUT) == 15

print("Part One: ", rps_score(INPUT))
