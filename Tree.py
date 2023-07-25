from __future__ import annotations

from typing import Union

class TreeNode:
    def __init__(self, val: any, left: TreeNode = None, right: TreeNode = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return (
            f"{self.val} -> ({self.left.val if self.left else None}, "
            f"{self.right.val if self.right else None})")


class BinarySearchTree:
    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def search(self, val : any) -> Union[TreeNode, bool]:
        def help_search(root, val):
            if not root:
                return False
            
            if val > root.val:
                return help_search(root.right, val)
            elif val < root.val:
                return help_search(root.left, val)
            else:
                return root
        
        return help_search(self.root, val)
        

if __name__ == "__main__":
    root = TreeNode(6,
        TreeNode(4,
            TreeNode(2),
            TreeNode(5)
        ), 
        TreeNode(9,
            TreeNode(8)
        ))
    tree = BinarySearchTree(root)

    target = 4
    print(f"Searching for {target}: {tree.search(target)}")