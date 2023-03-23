# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        center = len(nums) // 2
        
        node = TreeNode(nums[center])
        node.left = self.sortedArrayToBST(nums[:center])
        node.right = self.sortedArrayToBST(nums[center + 1:])

        return node