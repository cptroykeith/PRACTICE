class Solution:
    def isPalindrome(self, s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
        cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the cleaned string is a palindrome
        return cleaned_str == cleaned_str[::-1]