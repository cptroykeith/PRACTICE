class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
         # Calculate the effective k (in case k > len(nums))
        k = k % len(nums)
            
            # Split the list at the index len(nums) - k
        nums[:] = nums[-k:] + nums[:-k]