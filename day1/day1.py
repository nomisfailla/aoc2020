def load_input(filename):
    return [int(n) for n in open(filename, 'r').read().split()]

def solve2_brute(arr):
    for x in arr:
        for y in arr:
            if x + y == 2020:
                return x * y
    return 0

def solve3_brute(arr):
    for x in arr:
        for y in arr:
            for z in arr:
                if x + y + z == 2020:
                    return x * y * z
    return 0

arr = load_input("day1.input")
print(solve2_brute(arr))
print(solve3_brute(arr))
