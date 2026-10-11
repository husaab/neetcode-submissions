class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        # store the product of numbers to the left
        prefix_product = 1

        for current_index in range(len(nums)):
            output[current_index] = prefix_product
            prefix_product *= nums[current_index]

            # so in this scenari, on loop 1, we do output[0] = 1
            # then prefix_product = 1 * 1
            # then on loop 2, we do output[1] = 1
            # prefix_product *= 2
        
        suffix_product = 1

        for current_index in range(len(nums)-1, -1, -1):
            output[current_index] *= suffix_product
            suffix_product *= nums[current_index]
        
        return output