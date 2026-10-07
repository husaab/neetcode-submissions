# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_index = {}
        for i in range(len(inorder)):
            val_index[inorder[i]] = i
        
        def build(preorder_start, left, right):
            if left > right:
                return None

            root = TreeNode(preorder[preorder_start])

            mid = val_index[root.val]
            left_len = mid - left

            root.left = build(
                preorder_start + 1,
                left,
                mid - 1
            )

            root.right = build(
                preorder_start + 1 + left_len,
                mid + 1,
                right
            )

            return root

        return build(0, 0, len(inorder) - 1)