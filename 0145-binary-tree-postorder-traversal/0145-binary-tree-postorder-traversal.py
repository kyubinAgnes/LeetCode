# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = [(root, False)]
        while st:
            node, flag = st.pop()
            if node:
                if flag:
                    res.append(node.val)
                else:
                    st.append((node, True))
                    st.append((node.right, False))
                    st.append((node.left, False))
        return res
                    
                    
                    