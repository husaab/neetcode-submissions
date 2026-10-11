class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frequency_map = {}
        left = 0
        longest_length = 0

        for right in range(len(s)):
            current_character = s[right]

            frequency_map[current_character] = frequency_map.get(current_character, 0) + 1

            while (right - left + 1) - max(frequency_map.values()) > k:
                left_character = s[left]
                frequency_map[left_character] -=1
                left+=1
            
            window_length = right - left + 1
            longest_length = max(longest_length, window_length)
        
        return longest_length


        