from collections import Counter

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def parse(input: str):
    return [int(x) for x in input.strip().split(',')]

def part1(input: str) -> int:
    numbers = parse(input)

    numbers = sorted(numbers, reverse=True)
    numbers = set(numbers)

    return sum(numbers)

def part2(input: str) -> int:
    numbers = parse(input)

    numbers = sorted(numbers, reverse=True)
    numbers = list(set(numbers))

    return sum(numbers[-20:])

def part3(input: str) -> int:
    numbers = parse(input)

    numbers = Counter(numbers)

    return max(numbers.values())

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))















