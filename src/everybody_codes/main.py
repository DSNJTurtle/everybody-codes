import logging
import os

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")

os.environ["ECD_TOKEN"] = ""


def part1(input_string: str) -> str:
    pass


def part2(input_string: str) -> str:
    pass


if __name__ == "__main__":
    quest = 1
    event = 2024
    data = get_inputs(quest=quest, event=event)

    if True:
        print(data["1"])
        s1 = part1(data["1"])
        submit(quest=quest, event=event, part=1, answer=s1)

    if True:
        print(data["2"])
        s2 = part2(data["2"])
        submit(quest=quest, event=event, part=2, answer=s2)
