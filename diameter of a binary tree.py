# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0
            l = dfs(root.left)
            r = dfs(root.right)
            here = max(l[0],r[0])+1
            return here, max(l[1],r[1],l[0]+r[0]+1)
        res = dfs(root)[1]
        return res-1 if res > 0 else 0
        
'''
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.d = 0
        def dfs(node):
            if not node: return 0
            l, r = dfs(node.left), dfs(node.right)
            self.d = max(l + r, self.d)
            return 1 + max(l, r)
        dfs(root)
        return self.d

'''
