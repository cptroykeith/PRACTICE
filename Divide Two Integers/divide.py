def divide(dividend, divisor):
    if dividend == 0:
        return 0

    if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
        sign = 1
    else:
        sign = -1

    dividend = abs(dividend)
    divisor = abs(divisor)

    result = 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            result += i
            i <<= 1
            temp <<= 1

    result = result * sign

    return min(max(result, -2**31), 2**31 - 1)
