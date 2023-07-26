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

    @classmethod
    def fromValue(cls, val: any) -> BinarySearchTree:
        return cls(TreeNode(val))

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
    
    def insert(self, val: any) -> None:
        def help_insert(root: TreeNode, node: TreeNode) -> TreeNode:
            # Base Case: Leaf found - return the node to add it
            if not root:
                return node
            
            # Select subtree to follow - set child to the result of the call
            if node.val < root.val:
                root.left = help_insert(root.left, node)
            elif node.val > root.val:
                root.right = help_insert(root.right, node)
            return root # By default just return the existing child

        if not self.root: # Case: tree is empty
            self.root = TreeNode(val)
            return
        
        help_insert(self.root, TreeNode(val))
        

if __name__ == "__main__":
    tree = BinarySearchTree.fromValue(10)
    for val in [12, 15, 8, 2, 3, 14, 5]:
        tree.insert(val)

    target = 2
    print(f"Searching for {target}: {tree.search(target)}")