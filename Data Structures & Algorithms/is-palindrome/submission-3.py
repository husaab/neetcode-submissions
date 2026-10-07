class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = ""
        for character in s:
            if character.isalnum():
                sanitized+=character.lower()

        left = 0
        right = len(sanitized) - 1

        while left <= right:
            if sanitized[left] != sanitized[right]:
                return False

            left+=1
            right-=1
        
        return True
        