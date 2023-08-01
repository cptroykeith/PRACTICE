class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0
        current_length = 1
        
        for i in range(1, len(nums)):
            if nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                current_length += 1
            else:
                current_length = 1
            
            max_length = max(max_length, current_length)
        
        return max_length