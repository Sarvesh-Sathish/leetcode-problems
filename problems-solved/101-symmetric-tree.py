from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        elif root.left is None:
            return False
        elif root.right is None:
            return False
        return self.helper(root.left, root.right)
    def helper(self, leftNode, rightNode):
        
        print(leftNode.val, rightNode.val)
        if leftNode.left is None and leftNode.right is None and rightNode.left is None and rightNode.right is None:
            return leftNode.val == rightNode.val
        elif leftNode.left is not None and leftNode.right is not None and rightNode.left is not None and rightNode.right is not None:
            return leftNode.val == rightNode.val and self.helper(leftNode.left, rightNode.right) and self.helper(leftNode.right, rightNode.left)
        elif leftNode.left is not None and leftNode.right is None and rightNode.left is None and rightNode.right is not None:
            return leftNode.val == rightNode.val and self.helper(leftNode.left, rightNode.right)
        elif leftNode.left is None and leftNode.right is not None and rightNode.left is not None and rightNode.right is None:
            return leftNode.val == rightNode.val and self.helper(leftNode.right, rightNode.left)
        
        
        return False
