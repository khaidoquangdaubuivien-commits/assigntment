import random
d1 = random.randint(0, 9)
d2 = random.randint(0, 9)
d3 = random.randint(0, 9)
code1 = f"{d1}{d2}{d3}"
c1 = random.randint(1, 6)
c2 = random.randint(1, 6)
c3 = random.randint(1, 6)
c4 = random.randint(1, 6)
code2 = f"{c1}{c2}{c3}{c4}"
print(f"The 3-digit code is: {code1}")
print(f"The 4-digit code is: {code2}")