import time
def fibonacciRecursivo(n):
    if n==0 or n==1: 
        rpta = 1
    else: 
        if n<0:
            rpta = 0
        else: 
            rpta = fibonacciRecursivo(n-1)+ fibonacciRecursivo(n-2)
    return rpta
tiempo1 = time.perf_counter()
fibonacciRecursivo(10)
tiempo2 = time.perf_counter()
print("Fibonacci Recursivo demoro:", tiempo2-tiempo1)

def fibonacciNoRecursivo(n):
    if n==0 or n==1: 
        return  1
    else: 
        if n<0:
            return 0
        else: 
            return fibonacciNoRecursivo(n-1)+ fibonacciNoRecursivo(n-2)
tiempo1 = time.perf_counter()
fibonacciNoRecursivo(10)
tiempo2 = time.perf_counter()
print("Fibonacci no Recursivo demoro:", tiempo2-tiempo1)