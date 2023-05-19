def factorial(n):
    
    factorial = 1

    for i in range(n):
        factorial*=i+1

    return factorial

for i in range(10):
    print(factorial(i))
