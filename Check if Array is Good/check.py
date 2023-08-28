def isGoodArray(nums):
    max_num = max(nums)
    count_max_num = nums.count(max_num)
    
    if max_num != len(nums) - 1:
        return False
    
    if count_max_num != 2:
        return False
    
    return True

# Test the function with the given example
nums = [2, 1, 3]
print(isGoodArray(nums))  # Output: False
