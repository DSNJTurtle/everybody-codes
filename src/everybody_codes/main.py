import logging

import numpy as np
import shapely
from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    # input_string = """1,5,2,6,8,4,1,7,3"""
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 32
    step = 2 * np.pi / n_nails
    circle_positions = np.array([i * step for i in range(n_nails)])

    n_crosses = 0
    for a, b in zip(data, data[1:], strict=False):
        if np.abs(np.abs(circle_positions[b] - circle_positions[a]) - np.pi) < (np.pi / 180 * 2):
            n_crosses += 1

    return str(n_crosses)


def part2(input_string: str) -> str:
    # input_string = "1,5,2,6,8,4,1,7,3,5,7,8,2"
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 256
    step = 2 * np.pi / n_nails
    angles = np.array([np.pi / 2 - i * step for i in range(n_nails)])
    points = np.exp(1j * angles)

    previous_lines = []
    n_knots = 0
    for a, b in zip(data, data[1:], strict=False):
        pa = points[a]
        pb = points[b]
        ls = shapely.geometry.LineString([[pa.real, pa.imag], [pb.real, pb.imag]])

        for pl in previous_lines:
            if ls.crosses(pl):
                # make sure that the intersection does not occur on the circle
                x = list(shapely.intersection(ls, pl).coords)[0]
                x = x[1] + 1j * x[0]
                xp = np.abs(points - x) < 1e-3
                if not xp.any():
                    n_knots += 1

        previous_lines.append(ls)

    return str(n_knots)


def part3(input_string: str) -> str:
    # input_string = "1,5,2,6,8,4,1,7,3,6"
    data = np.array([int(x) for x in input_string.split(",")], dtype=int) - 1  # remove 1 counting offset

    n_nails = 256
    step = 2 * np.pi / n_nails
    angles = np.array([np.pi / 2 - i * step for i in range(n_nails)])
    points = np.exp(1j * angles)

    previous_lines = []
    for a, b in zip(data, data[1:], strict=False):
        pa = points[a]
        pb = points[b]
        ls = shapely.geometry.LineString([[pa.real, pa.imag], [pb.real, pb.imag]])
        previous_lines.append(ls)

    cuts = []
    for a in range(n_nails - 1):
        for b in range(a + 1, n_nails):
            pa = points[a]
            pb = points[b]
            ls = shapely.geometry.LineString([[pa.real, pa.imag], [pb.real, pb.imag]])

            n_threads = 0
            for pl in previous_lines:
                if ls.crosses(pl):
                    # make sure that the intersection does not occur on the circle
                    x = list(shapely.intersection(ls, pl).coords)[0]
                    x = x[1] + 1j * x[0]
                    xp = np.abs(points - x) < 1e-3
                    if not xp.any():
                        n_threads += 1
                elif pl.buffer(1e-2).contains(ls):
                    n_threads += 1

            cuts.append((a, b, n_threads))

    m = max([x[2] for x in cuts])
    return str(m)


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
