nums = [0,0,1,1,1,2,2,3,3,4]

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        insert_index = 1
        for i in range (1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1

        return insert_index
