import logging

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    data = [int(x) for x in input_string.split(",")]

    r = sorted(list(set(data)))
    r = sum(r)
    return str(r)


def part2(input_string: str) -> str:
    data = [int(x) for x in input_string.split(",")]

    r = sorted(list(set(data)))
    r = r[:20]
    r = sum(r)
    return str(r)


def part3(input_string: str) -> str:
    data = sorted([int(x) for x in input_string.split(",")])

    d = {}
    for i in data:
        d[i] = d.get(i, 0) + 1

    r = max(d.values())

    return str(r)


if __name__ == "__main__":
    quest = 3
    event = 2025
    data = get_inputs(quest=quest, event=event)

    s = part3(data["3"])
    print(f"Solution: {s}")
    if True:
        submit(quest=quest, event=event, part=3, answer=s)
