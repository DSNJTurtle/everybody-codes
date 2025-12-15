import functools
import logging

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    # input_string = """ABabACacBCbca"""

    n_match = 0
    for i, s in enumerate(input_string):
        if s == "A":
            for j in range(i + 1, len(input_string)):
                if input_string[j] == "a":
                    n_match += 1
    return str(n_match)


def part2(input_string: str) -> str:
    # input_string = """ABabACacBCbca"""

    matches = {}
    for i, s in enumerate(input_string):
        if s.isupper():
            for j in range(i + 1, len(input_string)):
                if input_string[j] == s.lower():
                    matches[s] = matches.get(s, 0) + 1

    return str(sum(matches.values()))


def part3(input_string: str) -> str:
    # input_string = """AABCBABCABCabcabcABCCBAACBCa"""
    ll = len(input_string)
    repeat = 1000
    offset = 1000
    mm = repeat * ll

    def _is(pos: int) -> str:
        return input_string[pos % ll]

    @functools.cache
    def get_count(pos: int) -> int:
        n_matches = 0
        s = _is(pos)
        if s.islower():
            for j in range(pos - offset, pos + offset + 1):
                if _is(j) == s.upper():
                    n_matches += 1
        return n_matches

    n_matches = 0
    for i in range(mm + 1):
        if offset < i < mm - offset:
            n_matches += get_count(i % ll)
        else:
            s = _is(i)
            if s.islower():
                imin = max(0, i - offset)
                imax = min(i + offset + 1, mm)
                for j in range(imin, imax):
                    if _is(j) == s.upper():
                        n_matches += 1

    return str(n_matches)


if __name__ == "__main__":
    quest = 6
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
