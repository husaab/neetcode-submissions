class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        curr_char_index = {}
        max_length = 0

        left = 0
        right = 0

        while right < len(s):
            curr_char = s[right]

            if curr_char in curr_char_index and curr_char_index[curr_char] >= left:
                left = curr_char_index[curr_char] + 1
            
            curr_char_index[curr_char] = right
            max_length = max(max_length, right - left + 1)
            right+=1
        
        return max_length 


        
        