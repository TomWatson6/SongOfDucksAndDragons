
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def parse(input: str):
    components = {}

    letter, numbers = input.strip().split("=")
    components[letter] = [int(x) for x in numbers[1:-1].split(',')]

    return components

def add(x1, y1, x2, y2):
    return [x1 + x2, y1 + y2]

def mult(x1, y1, x2, y2):
    return [x1 * x2 - y1 * y2, x1 * y2 + y1 * x2]

def div(x1, y1, x2, y2):
    return [c1 // c2 if c1 >= 0 else -((-c1) // c2) for c1, c2 in zip([x1, y1], [x2, y2])]

def output(component):
    return f"[{component[0]},{component[1]}]"

def part1(input: str) -> int:
    components = parse(input)

    curr = [0, 0]

    for _ in range(3):
        curr = mult(curr[0], curr[1], curr[0], curr[1])
        curr = div(curr[0], curr[1], 10, 10)
        curr = add(curr[0], curr[1], components['A'][0], components['A'][1])

    return output(curr)

def part2(input: str) -> int:
    components = parse(input)
    comp = components['A']
    considerations = []
    bound = 1_000_000
    valid = 0

    for r in range(101):
        for c in range(101):
            considerations.append([comp[0] + r * 10, comp[1] + c * 10])

    for con in considerations:
        result = [0, 0]
        v = True

        for i in range(100):
            result = mult(result[0], result[1], result[0], result[1])
            result = div(result[0], result[1], 100_000, 100_000)
            result = add(result[0], result[1], con[0], con[1])
            if any(abs(num) > bound for num in result):
                v = False
                break

        if v:
            valid += 1


    return valid

def part3(input: str) -> int:
    components = parse(input)
    comp = components['A']
    considerations = []
    bound = 1_000_000
    valid = 0

    for r in range(1001):
        for c in range(1001):
            considerations.append([comp[0] + r, comp[1] + c])

    for con in considerations:
        result = [0, 0]
        v = True

        for i in range(100):
            result = mult(result[0], result[1], result[0], result[1])
            result = div(result[0], result[1], 100_000, 100_000)
            result = add(result[0], result[1], con[0], con[1])
            if any(abs(num) > bound for num in result):
                v = False
                break

        if v:
            valid += 1


    return valid

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))















