#Dec 6, 2022
#James Crisp

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        final = []

        def traverse(rooter):
            if rooter is None: return
            
            final.append(rooter.val)
            traverse(rooter.left)
            traverse(rooter.right)
        
        traverse(root)
        return final