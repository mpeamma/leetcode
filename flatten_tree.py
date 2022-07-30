# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def print(self):
        current = self
        while current.right is not None:
            print(current.val)
            current = current.right
        print(current.val)

class Solution:
    def add_to_end(self, root, addition):
        current = root
        if addition is not None and root is not None:
            while current.right is not None:
                current = current.right

            current.right = addition

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            right = root.right
            if root.left is not None:
                root.right = root.left
                self.flatten(root.right)
                self.flatten(right)
                self.add_to_end(root.right, right)
            else:
                self.flatten(right)
                root.right = right
            root.left = None


tree =  TreeNode(1,
            TreeNode(2,
                TreeNode(3),
                TreeNode(4)),
            TreeNode(5,
                None,
                TreeNode(6)))

Solution().flatten(tree)

tree.print()