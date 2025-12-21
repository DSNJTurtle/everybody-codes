import logging
from dataclasses import dataclass, field

from ecd import get_inputs, submit

logger = logging.getLogger("everybody_codes")


def hamming_distance(c: str, p1: str, p2: str) -> tuple[int, int]:
    if len(c) != len(p2) or len(c) != len(p2):
        return -1, -1

    n_matches_p1 = 0
    n_matches_p2 = 0
    for i in range(len(c)):
        if not (c[i] == p1[i] or c[i] == p2[i]):
            return -1, -1

        if c[i] == p1[i]:
            n_matches_p1 += 1
        if c[i] == p2[i]:
            n_matches_p2 += 1

    return n_matches_p1, n_matches_p2


def part1(input_string: str) -> str:
    data = {}
    for x in input_string.splitlines():
        n, seq = x.split(":", 1)
        data[n] = seq

    for ck in data:
        parent_keys = [x for x in data if x != ck]
        assert len(parent_keys) == 2
        c = data[ck]
        p1 = data[parent_keys[0]]
        p2 = data[parent_keys[1]]

        n1, n2 = hamming_distance(c, p1, p2)
        if n1 != -1 and n2 != -1:
            return str(n1 * n2)

    return ""


def part2(input_string: str) -> str:
    data = {}
    for x in input_string.splitlines():
        n, seq = x.split(":", 1)
        data[n] = seq

    keys = list(data.keys())
    results = []
    for i, ck in enumerate(keys):
        for j, p1k in enumerate(keys):
            if i == j:
                continue
            for k in range(j + 1, len(keys)):
                p2k = keys[k]
                if ck == p2k:
                    continue

                c = data[ck]
                p1 = data[p1k]
                p2 = data[p2k]

                n1, n2 = hamming_distance(c, p1, p2)
                if n1 != -1 and n2 != -1:
                    results.append(n1 * n2)

    return str(sum(results))


@dataclass
class Duck:
    """Duck."""

    scale_number: int
    dna: str
    parents: list["Duck"] = field(default_factory=list)
    children: list["Duck"] = field(default_factory=list)

    def build_tree(self, ids: set[int] | None = None) -> set[int]:
        ids = ids or set()

        if self.scale_number in ids:
            return ids

        ids.add(self.scale_number)
        for p in self.parents:
            for i in p.build_tree(ids=ids):
                ids.add(i)

        for child in self.children:
            for i in child.build_tree(ids=ids):
                ids.add(i)

        return ids


def part3(input_string: str) -> str:
    ducks: dict[int, Duck] = {}
    for x in input_string.splitlines():
        n, seq = x.split(":", 1)
        ducks[int(n)] = Duck(int(n), seq)

    keys = list(ducks.keys())
    for i, ck in enumerate(keys):
        for j, p1k in enumerate(keys):
            if i == j:
                continue
            for k in range(j + 1, len(keys)):
                p2k = keys[k]
                if ck == p2k:
                    continue

                c = ducks[ck]
                p1 = ducks[p1k]
                p2 = ducks[p2k]

                n1, n2 = hamming_distance(c.dna, p1.dna, p2.dna)
                if n1 != -1 and n2 != -1:
                    c.parents.extend([p1, p2])
                    p1.children.append(c)
                    p2.children.append(c)

    roots = [x for x in ducks if ducks[x].parents == []]
    trees = [ducks[x].build_tree() for x in roots]
    trees = sorted(trees, key=lambda x: len(x), reverse=True)
    tree = trees[0]
    result = 0
    for i in tree:
        result += i

    return str(result)


if __name__ == "__main__":
    quest = 9
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
