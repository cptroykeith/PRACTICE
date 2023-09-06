def maxSumOfPairWithEqualMaxDigit(nums):
    max_sum = -1
    max_digits = [0] * 10  # Initialize a list to store the maximum numbers for each digit (0-9)

    for num in nums:
        max_digit = int(max(str(num)))  # Find the maximum digit in the current number
        max_digits[max_digit] = max(max_digits[max_digit], num)  # Store the maximum number for that digit

    for i in range(1, 10):
        for j in range(i + 1, 10):
            if max_digits[i] != 0 and max_digits[j] != 0:
                max_sum = max(max_sum, max_digits[i] + max_digits[j])

    return max_sum


