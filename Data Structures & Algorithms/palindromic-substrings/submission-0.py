class Solution:
    def countSubstrings(self, s: str) -> int:
        # return number of substrings within s that are palindromes

        string_length = len(s)

        is_palindrome = [
            [False] * string_length
            for _ in range(string_length)
        ]
        
        result = 0

        for substring_length in range(1, string_length + 1):
            number_of_starting_positions = (
                string_length - substring_length + 1
            )
            # say we are at substirng length 1, then our numbe rof strating positions is 3 if strign length is 3
            # say we are at substirng 2, then we can only start at 2 in the scenario that our string length is 4
            # say we are at substring 3, we can legit only start at 1 , which makes sense
            for start_index in range(number_of_starting_positions):
                end_index = start_index + substring_length - 1
                # end index is going to be 0 + 3 - 1 = 2
                # so our end index here is 2 which establishes how deep we can go

                outer_characters_match = (
                    s[start_index] == s[end_index]
                )

                if substring_length == 1:
                    is_palindrome[start_index][end_index] = True
                elif substring_length == 2:
                    is_palindrome[start_index][end_index] = (
                        outer_characters_match
                    )
                else:
                    is_palindrome[start_index][end_index] = (
                        outer_characters_match and
                        is_palindrome[start_index+1][end_index-1]
                    )
                
                if is_palindrome[start_index][end_index]:
                    result+=1

        return result


