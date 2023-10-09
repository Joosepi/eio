A, B, C, D = map(float, input("Enter the values of A, B, C, and D: ").split())

warm_energy = C * 60

cool_time = (100 - 22) / D

cool_energy = A * cool_time * B + A * (100 - 22)

print(round(warm_energy, 2))
print(round(cool_energy, 2))