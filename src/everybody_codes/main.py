import logging
from dataclasses import dataclass
from functools import cmp_to_key

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


@dataclass
class Node:
    """Node."""

    spine: int
    left: int | None = None
    right: int | None = None
    next_node: "Node|None" = None

    def add(self, i: int) -> None:

        n = self
        while n.next_node is not None:
            n = n.next_node

        if i < self.spine and self.left is None:
            self.left = i
        elif i > self.spine and self.right is None:
            self.right = i
        else:
            if self.next_node is None:
                self.next_node = Node(i)
            else:
                self.next_node.add(i)

    def get_quality(self) -> str:
        res = ""
        n = self
        while True:
            res = res + str(n.spine)
            n = n.next_node
            if n is None:
                break

        return res

    def get_levels(self) -> list[int]:
        res = []
        n = self
        while n is not None:
            i = (
                (str(n.left) if n.left is not None else "")
                + str(n.spine)
                + (str(n.right) if n.right is not None else "")
            )
            res.append(int(i))
            n = n.next_node

        return res


def part1(input_string: str) -> str:
    n, numbers = input_string.split(":", 1)
    numbers = [int(x) for x in numbers.strip().split(",")]

    node = Node(numbers.pop(0))
    while numbers:
        nn = numbers.pop(0)
        node.add(nn)

    return node.get_quality()


def part2(input_string: str) -> str:
    d = {}
    for line in input_string.splitlines():
        identifier, numbers = line.split(":", 1)
        identifier = int(identifier)
        numbers = [int(x) for x in numbers.strip().split(",")]

        node = Node(numbers.pop(0))
        while numbers:
            nn = numbers.pop(0)
            node.add(nn)

        q = node.get_quality()
        d[identifier] = q

    _max = max([int(x) for x in d.values()])
    _min = min([int(x) for x in d.values()])

    diff = _max - _min

    return str(diff)


def _order(s1: tuple[int, Node], s2: tuple[int, Node]) -> int:
    q1 = int(s1[1].get_quality())
    q2 = int(s2[1].get_quality())

    if q1 < q2:
        return 1
    elif q1 > q2:
        return -1
    else:
        l1 = s1[1].get_levels()
        l2 = s2[1].get_levels()
        for i1, i2 in zip(l1, l2, strict=True):
            if i1 < i2:
                return 1
            elif i1 > i2:
                return -1

        if s1[0] < s2[0]:
            return 1
        elif s1[0] > s2[0]:
            return -1
        else:
            return 0


def part3(input_string: str) -> str:
    swords = []
    for line in input_string.splitlines():
        identifier, numbers = line.split(":", 1)
        identifier = int(identifier)
        numbers = [int(x) for x in numbers.strip().split(",")]

        node = Node(numbers.pop(0))
        while numbers:
            nn = numbers.pop(0)
            node.add(nn)

        swords.append((identifier, node))

    swords = sorted(swords, key=cmp_to_key(_order))
    checksum = 0
    for i, s in enumerate(swords):
        checksum += (i + 1) * s[0]

    return str(checksum)


if __name__ == "__main__":
    quest = 5
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
