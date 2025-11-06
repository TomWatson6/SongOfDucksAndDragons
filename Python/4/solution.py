from math import floor, ceil

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def parse(input: str):
    return [int(x) for x in input.splitlines()]

def parse2(input: str):
    return [x for x in input.splitlines()]

def part1(input: str) -> int:
    cogs = parse(input)

    turns = 2025

    for i in range(len(cogs) - 1):
        turns *= cogs[i]
        turns /= cogs[i + 1]

    return floor(turns)

def part2(input: str) -> int:
    cogs = parse(input)

    turns = 10000000000000

    for i in range(len(cogs) - 1, 0, -1):
        turns *= cogs[i]
        turns /= cogs[i - 1]

    return ceil(turns)

def part3(input: str) -> int:
    cogs = parse2(input)

    turns = 100

    for i in range(len(cogs) - 1):
        left, right = [int(x) for x in cogs[i].split("|")], [int(x) for x in cogs[i + 1].split("|")]
        if len(left) == 1:
            turns *= left[0]
            turns /= right[0]
            continue
        if len(right) == 1:
            turns *= left[1]
            turns /= right[0]
            continue

        turns *= left[1]
        turns /= right[0]

    return floor(turns)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))















