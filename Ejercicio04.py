import time
def factorialRecursivo(num):
    if num == 0 or num == 1:
        respuesta = 1
    else:
        respuesta = num*factorialRecursivo(num-1)
    return respuesta
tiempo1 = time.perf_counter()
factorialRecursivo(9)
tiempo2=time.perf_counter()
print("Factorial Recursivo demoró", tiempo2-tiempo1)

def factorialNoRecursivo(num):
    if num == 0 or num == 1:
        return 1
    else:
       return num*factorialNoRecursivo(num-1)
tiempo1 = time.perf_counter()
factorialNoRecursivo(9)
tiempo2 = time.perf_counter()
print("Factorial no recursivo demoró ", tiempo2-tiempo1)