import functools
import logging

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def part1(input_string: str) -> str:
    names, rule_str = input_string.split("\n\n")
    names = names.split(",")

    rules = {}
    for r in rule_str.splitlines():
        lhs, rhs = r.split(">")
        lhs = lhs.strip()
        rhs = rhs.strip().split(",")
        rules[lhs] = rhs

    for name in names:
        valid = True
        for i in range(1, len(name)):
            s1 = name[i - 1]
            s2 = name[i]
            if (r1 := rules.get(s1)) is None:
                valid = False
                break
            else:
                if s2 not in r1:
                    valid = False
                    break

        if valid:
            return name

    return ""


def part2(input_string: str) -> str:
    names, rule_str = input_string.split("\n\n")
    names = names.split(",")

    rules = {}
    for r in rule_str.splitlines():
        lhs, rhs = r.split(">")
        lhs = lhs.strip()
        rhs = rhs.strip().split(",")
        rules[lhs] = rhs

    valid_names = 0
    for idx, name in enumerate(names):
        valid = True
        for i in range(1, len(name)):
            s1 = name[i - 1]
            s2 = name[i]
            if (r1 := rules.get(s1)) is None:
                valid = False
                break
            else:
                if s2 not in r1:
                    valid = False
                    break

        if valid:
            valid_names += idx + 1

    return str(valid_names)


def is_valid_name(name: str, rules: dict) -> bool:
    for i in range(1, len(name)):
        s1 = name[i - 1]
        s2 = name[i]
        if (r1 := rules.get(s1)) is None:
            return False
        else:
            if s2 not in r1:
                return False

    return True


def part3(input_string: str) -> str:
    names, rule_str = input_string.split("\n\n")

    rules = {}
    for r in rule_str.splitlines():
        lhs, rhs = r.split(">")
        lhs = lhs.strip()
        rhs = rhs.strip().split(",")
        rules[lhs] = rhs

    @functools.cache
    def get_suffixes(s: str, remaining_length: int) -> list[str]:
        if remaining_length == 0:
            return [""]

        suffixes = []
        for r in rules[s]:
            for suffix in get_suffixes(r, remaining_length - 1):
                extended_suffix = r + suffix
                suffixes.append(extended_suffix)

        return suffixes

    names = [x for x in names.split(",") if is_valid_name(x, rules)]
    finished_names = set()
    for name in names:
        suffixes = get_suffixes(name[-1], 11 - len(name))
        for s in suffixes:
            nn = name + s
            assert len(nn) == 11, "all names should have exactly 11 chars now"
            for i in range(7, len(nn) + 1):
                # add all valid names with at least 7 and up to 11 chars
                finished_names.add(nn[:i])

    return str(len(finished_names))


if __name__ == "__main__":
    quest = 7
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
