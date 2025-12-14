import logging

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    parts = input_string.split("\n\n")
    names, instructions = parts[0].split(","), parts[1].split(",")

    pos = 0
    ll = len(names)
    while instructions:
        i = instructions.pop(0)
        d, n = 1 if i.startswith("R") else -1, int(i[1:])
        n = d * n
        pos += n
        pos = min(max(pos, 0), ll - 1)

    return names[pos]


def part2(input_string: str) -> str:
    parts = input_string.split("\n\n")
    names, instructions = parts[0].split(","), parts[1].split(",")

    pos = 0
    ll = len(names)
    while instructions:
        i = instructions.pop(0)
        d, n = 1 if i.startswith("R") else -1, int(i[1:])
        n = d * n
        pos += n
        pos = pos % ll

    return names[pos]


def part3(input_string: str) -> str:
    parts = input_string.split("\n\n")
    names, instructions = parts[0].split(","), parts[1].split(",")

    pos = 0
    ll = len(names)
    while instructions:
        i = instructions.pop(0)
        d, n = 1 if i.startswith("R") else -1, int(i[1:])
        n = d * n
        pos += n
        pos = pos % ll

        old_name = names[0]
        names[0] = names[pos]
        names[pos] = old_name
        pos = 0

    return names[pos]


if __name__ == "__main__":
    quest = 1
    event = 2025
    data = get_inputs(quest=quest, event=event)

    s = part3(data["3"])
    print(f"Solution: {s}")
    if True:
        submit(quest=quest, event=event, part=3, answer=s)
