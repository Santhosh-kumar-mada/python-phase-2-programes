from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inorder_successor(curr):
            curr = curr.right
            while curr and curr.left:
                curr = curr.left
            return curr
        def deletion(root,key):
            if not root:
                return root
            if key<root.val:
                root.left = deletion(root.left,key)
            elif key>root.val:
                root.right = deletion(root.right,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                successor = inorder_successor(root)
                root.val = successor.val
                root.right = deletion(root.right,successor.val)
            return root
        return deletion(root,key)