A, B = map(int, input().split())

if A == 0:
    output = str(B)
elif B == 0:
    output = "x" if A == 1 else "-x" if A == -1 else str(A) + "x"
else:
    if A == 1:
        output = "x+" + str(B)
    elif A == -1:
        output = "-x+" + str(B)
    else:
        output = str(A) + "x+" + str(B)

print(output)