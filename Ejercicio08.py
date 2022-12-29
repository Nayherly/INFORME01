def potencialRecursivo(a,b):
    if b==1:
        rpta = a
    else:
        if b%2 == 0:
            pot = potencialRecursivo(a,int(b/a))
            rpta= pot*pot
        else:
            rpta = a*potencialRecursivo(a,b-1)
    return rpta
print(potencialRecursivo(9,10))