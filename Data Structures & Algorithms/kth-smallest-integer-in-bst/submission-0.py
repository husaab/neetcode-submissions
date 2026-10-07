# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return the k'th smallest value in the tree
        # i'm thinking of basically going through the bst
        # i keep going left left left
        # and then when i hit the deepest left
        # i start recursively appending it to the result

        # and then after recursively appending it to result
        # i just use k to fetch k's smallest by doing len(result) - k for example
        # so we want to solve this in order,
        # and we can just grab result[k]

        if not root:
            return None

        result = []
        
        def reverse_inorder(node):
            if not node:
                return
            
            reverse_inorder(node.left)

            result.append(node.val)

            reverse_inorder(node.right)

        
        reverse_inorder(root)
        return result[k-1]


        