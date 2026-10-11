class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded+= str(len(word)) + "#" + word

        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        current_index = 0

        while current_index < len(s):
            length_end_index = current_index

            while s[length_end_index] != "#":
                length_end_index+=1
            
            word_length = int(s[current_index:length_end_index])
            word_start_index = length_end_index + 1
            word_end_index = word_start_index + word_length
            
            result.append(s[word_start_index:word_end_index])

            current_index = word_end_index
        
        return result