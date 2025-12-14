import logging

import numpy as np
from ecd import get_inputs, submit
from matplotlib import pyplot as plt

logger = logging.getLogger("everybody_codes")


def _divide(a: complex, b: complex) -> complex:
    _a = int(a.real / b.real)
    _b = int(a.imag / b.imag)
    return complex(_a, _b)


def part1(input_string: str) -> str:
    parts = eval(input_string.replace("A=", ""))
    a = complex(parts[0], parts[1])

    res = complex(0, 0)
    for _ in range(3):
        res *= res
        res = _divide(res, complex(10, 10))
        res += a

    return str([int(res.real), int(res.imag)]).replace(" ", "")


def compute(input_string: str, step: int, n_steps: int) -> str:
    parts = eval(input_string.replace("A=", ""))
    a = complex(parts[0], parts[1])

    grid = []
    n_engraved = 0
    for i in range(n_steps):
        row = []
        for j in range(n_steps):
            pos = a + step * j * 1j + step * i

            res = complex(0, 0)
            stopped = False
            for _ in range(100):
                res *= res
                res = _divide(res, complex(100_000, 100_000))
                res += pos

                if abs(res.real) > 1000000 or abs(res.imag) > 1000000:
                    stopped = True
                    row.append(0)
                    break

            if not stopped:
                n_engraved += 1
                row.append(1)

        grid.append(row)

    if True:
        _g = np.array(grid, dtype=int) * 256
        plt.imshow(_g, cmap="gray", interpolation="nearest")
        plt.show()

    return str(n_engraved)


def part2(input_string: str) -> str:
    return compute(input_string, 10, 101)


def part3(input_string: str) -> str:
    return compute(input_string, 1, 1001)


if __name__ == "__main__":
    quest = 2
    event = 2025
    data = get_inputs(quest=quest, event=event)

    s = part3(data["3"])
    print(f"Solution: {s}")
    if True:
        submit(quest=quest, event=event, part=3, answer=s)
