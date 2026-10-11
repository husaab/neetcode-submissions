class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        num_set = set(nums)
        current_length = 0

        for num in num_set:
            if num-1 not in num_set:
               current_number = num
               current_length = 1

               while current_number + 1 in num_set:
                    current_number+= 1
                    current_length+=1
                
               longest = max(longest, current_length)
            

        return longest
        
