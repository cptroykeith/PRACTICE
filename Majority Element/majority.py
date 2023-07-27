def majority_element(nums):
    # Initialize the candidate and count variables
    candidate = None
    count = 0
    
    # Find the majority element using Boyer-Moore Voting Algorithm
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate