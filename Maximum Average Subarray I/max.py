class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])  # Initialize the sum of the first k elements
        max_sum = window_sum  # Initialize the maximum sum as the sum of the first k elements

        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]  # Update the window sum by adding the next element and subtracting the first element
            max_sum = max(max_sum, window_sum)  # Update the maximum sum if the current sum is greater

        return max_sum / k  # Return the maximum average