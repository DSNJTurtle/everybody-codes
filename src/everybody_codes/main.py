import logging

import numpy as np
from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    # input_string = """1,5,2,6,8,4,1,7,3"""
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 32
    n_half = n_nails // 2

    n_crosses = 0
    for a, b in zip(data, data[1:], strict=False):
        if (a + n_half == b) or (b + n_half == a):
            n_crosses += 1

    return str(n_crosses)


def part2(input_string: str) -> str:
    # input_string = "1,5,2,6,8,4,1,7,3,5,7,8,2"
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 256
    threads = []
    n_knots = 0
    for a, b in zip(data, data[1:], strict=False):
        for t in threads:
            m1, m2 = min(t), max(t)
            m1, m2 = m1 - m1, m2 - m1
            n1, n2 = (a - m1) % n_nails, (b - m1) % n_nails
            n1, n2 = min(n1, n2), max(n1, n2)

            if m1 < n1 < m2 and n2 > m2:
                n_knots += 1

        threads.append((a, b))

    return str(n_knots)


def part3(input_string: str) -> str:
    # input_string = "1,5,2,6,8,4,1,7,3,6"
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 256
    state = {}
    for a, b in zip(data, data[1:], strict=False):
        state[a] = state.get(a, []) + [b]
        state[b] = state.get(b, []) + [a]

    n_cuts = -1
    for c1 in range(n_nails - 1):
        for c2 in range(c1 + 1, n_nails):
            _c = 0
            for start in range(c1 + 1, c2):
                for end in state.get(start, []):
                    if end < c1 or end > c2:
                        _c += 1

            if c2 in state.get(c1, []):
                # check if same thread is cutted
                _c += 1

            n_cuts = max(n_cuts, _c)

    return str(n_cuts)


if __name__ == "__main__":
    quest = 8
    event = 2025
    p = 3
    data = get_inputs(quest=quest, event=event)

    s = ""
    match p:
        case 1:
            s = part1(data["1"])
        case 2:
            s = part2(data["2"])
        case 3:
            s = part3(data["3"])

    print(f"Solution: {s}")
    if True:
        submit(quest=quest, event=event, part=p, answer=s)
