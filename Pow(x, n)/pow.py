def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    half = myPow(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

# Example Usage:
result1 = myPow(2.00000, 10)
result2 = myPow(2.10000, 3)
result3 = myPow(2.00000, -2)

print(result1)  # Output: 1024.00000
print(result2)  # Output: 9.26100
print(result3)  # Output: 0.25000
