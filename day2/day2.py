class Password:
    def __init__(self, line):
        parts = line.split(": ")
        self.password = parts[1]
        parts = parts[0].split(" ")
        self.policy_character = parts[1][0]
        parts = parts[0].split("-")
        self.policy_min = int(parts[0])
        self.policy_max = int(parts[1])

    def is_valid_range(self):
        n = 0
        for c in self.password:
            if c == self.policy_character:
                n += 1
        return n >= self.policy_min and n <= self.policy_max

    def is_valid_pos(self):
        return (
            self.password[self.policy_min - 1] == self.policy_character
        ) != (
            self.password[self.policy_max - 1] == self.policy_character
        )

def load_input(filename):
    return [Password(n.strip()) for n in open(filename, 'r').readlines()]

arr = load_input("day2.input")
n1 = 0
n2 = 0
for p in arr:
    if p.is_valid_range():
        n1 += 1
    if p.is_valid_pos():
        n2 += 1

print("P1:", n1, "valid passwords")
print("P2:", n2, "valid passwords")
