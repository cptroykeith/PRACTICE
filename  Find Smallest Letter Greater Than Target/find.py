class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # Perform a binary search
        left = 0
        right = len(letters) - 1
        result = letters[0]  # Set default result to the first character
        
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                result = letters[mid]
                right = mid - 1
        
        return result