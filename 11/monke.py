from util import christmas_input

INPUT = christmas_input.file_to_array('input.txt')
TEST_INPUT = christmas_input.file_to_array('test_input.txt')


def parse_instructs(initial_state):
    monkeys = []
    chunked = [initial_state[i * 7:(i + 1) * 7] for i in range((len(initial_state) + 7 - 1) // 7)]
    idx = 0
    for chunk in chunked:
        monkey = {
            "items": [int(i) for i in chunk[1].split(": ")[1].split(", ")],
            "operation": {
                "op": chunk[2].split(" ")[-2],
                "value": chunk[2].split(" ")[-1],
            },
            "test": int(chunk[3].split(" ")[-1]),
            "true_case": int(chunk[4].split(" ")[-1]),
            "false_case": int(chunk[5].split(" ")[-1]),
            "inspect_count": 0
        }
        print(monkey)
        monkeys.append(monkey)
        idx += 1

    return monkeys


def run_game(monkeys, calm_monkeys=True):
    total_rounds = 20 if calm_monkeys else 10000
    for round_number in range(total_rounds):
        monkey_num = 0
        for monkey in monkeys:
            monkey_num += 1
            while len(monkey["items"]) > 0:
                monkey["inspect_count"] += 1
                # Operate
                if monkey["operation"]["value"] == "old":
                    value = monkey["items"][0]
                else:
                    value = int(monkey["operation"]["value"])
                if monkey["operation"]["op"] == "*":
                    monkey["items"][0] *= value
                else:
                    monkey["items"][0] += value

                # Reduce
                if calm_monkeys:
                    monkey["items"][0] = (monkey["items"][0] // 3)

                # Fling
                if monkey["items"][0] % monkey["test"] == 0:
                    destination = monkey["true_case"]
                else:
                    destination = monkey["false_case"]
                monkeys[destination]["items"].append(monkey["items"].pop(0))
        if round_number % 100 == 0:
            print("  -- ROUND", round_number)
    return monkeys


def monkey_business(commands,  calm_monkeys=True):
    state = parse_instructs(commands)
    state = run_game(state, calm_monkeys)
    inspections = [monkey["inspect_count"] for monkey in state]
    top = sorted(inspections, reverse=True)[:2]
    total = top[0] * top[1]
    return total


assert monkey_business(TEST_INPUT) == 10605
print("Part One: ", monkey_business(INPUT))

assert monkey_business(TEST_INPUT, calm_monkeys=False) == 2713310158
print("Part Two: ", monkey_business(INPUT), calm_monkeys=False)