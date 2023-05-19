def Fibonacci(n):

    if n in (1,2):
        return 1
    
    return Fibonacci(n-1) + Fibonacci(n-2)

for i in range(1,10):
    print(Fibonacci(i))