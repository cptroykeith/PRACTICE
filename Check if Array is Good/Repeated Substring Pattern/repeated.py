class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
    
        # Iterate through possible substring lengths
        for i in range(1, n // 2 + 1):
            if n % i == 0:  # Check if it's a valid substring length
                substring = s[:i]
                
                # Check if repeating the substring forms the original string
                if substring * (n // i) == s:
                    return True
                
        return False