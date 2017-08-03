# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder)>0:
            root = TreeNode(preorder[0])
            index = inorder.index(root.val)
            
            root.left = self.buildTree(preorder[1:index+1], inorder[:index+1])
            root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
            
            return root
        else:
            return None