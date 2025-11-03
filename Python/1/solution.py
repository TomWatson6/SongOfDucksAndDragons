
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def parse(input: str):
    names, _, instructions = input.splitlines()

    names = [x.strip() for x in names.split(',')]
    instructions = [x.strip() for x in instructions.split(',')]

    return names, instructions

def part1(input: str) -> int:
    names, instructions = parse(input)

    i = 0

    for ins in instructions:
        dir, mag = ins[0], int(ins[1:])
        if dir == 'L':
            i -= mag
            i = max(i, 0)
        elif dir == 'R':
            i += mag
            i = min(len(names) - 1, i)

    return names[i]

def part2(input: str) -> int:
    names, instructions = parse(input)

    i = 0

    for ins in instructions:
        dir, mag = ins[0], int(ins[1:])
        if dir == 'L':
            i = (i - mag) % len(names)
        elif dir == 'R':
            i = (i + mag) % len(names)

    return names[i]

def part3(input: str) -> int:
    names, instructions = parse(input)

    for ins in instructions:
        dir, mag = ins[0], int(ins[1:])
        swp = 0
        if dir == 'L':
            swp = -mag % len(names)
        elif dir == 'R':
            swp = mag % len(names)

        names[0], names[swp] = names[swp], names[0]

    return names[0]

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))















