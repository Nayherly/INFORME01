def robot(n):
    if n == 1 or n==2:
        rpta = n
    else:
        rpta = robot(n-1)+robot(n-2)
    return rpta
metros = int(input("Ingrese los metros que el robot caminará: "))
for i in range(1,metros+1):
    print(robot(i))