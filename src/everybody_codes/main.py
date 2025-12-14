import logging

import numpy as np
from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    data = [int(x) for x in input_string.splitlines()]
    ratios = [data[i + 1] / data[i] for i in range(len(data) - 1)]
    total_ratio = np.prod(ratios)

    n_rotations = int(2025 / total_ratio)

    return str(n_rotations)


def part2(input_string: str) -> str:
    data = [int(x) for x in input_string.splitlines()]
    ratios = [data[i + 1] / data[i] for i in range(len(data) - 1)]
    total_ratio = np.prod(ratios)

    n_rotations = total_ratio * 10000000000000
    offset = 1 if int(n_rotations * 10) - int(n_rotations) > 0 else 0
    n_rotations = int(n_rotations) + offset

    return str(n_rotations)


def part3(input_string: str) -> str:
    data = input_string.splitlines()
    n_rotations = 100
    ratios = []
    for i in range(1, len(data)):
        a = data[i - 1]
        a = int(a.split("|", 1)[1]) if "|" in a else int(a)
        b = data[i]
        reached_end = "|" in b or i == len(data) - 1
        b = int(b.split("|", 1)[0]) if "|" in b else int(b)

        ratios.append(b / a)
        if not reached_end:
            continue
        else:
            r = np.prod(ratios)
            n_rotations = n_rotations / r
            ratios = []

    return str(int(n_rotations))


if __name__ == "__main__":
    quest = 4
    event = 2025
    data = get_inputs(quest=quest, event=event)

    s = part3(data["3"])
    print(f"Solution: {s}")
    if True:
        submit(quest=quest, event=event, part=3, answer=s)
