from __future__ import annotations

from collections import deque
from typing import List, Union

class TreeNode:
    def __init__(self, val: any, left: TreeNode = None, right: TreeNode = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return (
            f"{self.val} -> ({self.left.val if self.left else None}, "
            f"{self.right.val if self.right else None})")
    
    def __repr__(self) -> str:
        return str(self.val)


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


    def remove(self, val: any) -> None:
        def help_remove(root, val):
            if not root:
                return None
            
            # Locate the node to remove
            if val > root.val:
                root.right = help_remove(root.right, val)
            elif val < root.val:
                root.left = help_remove(root.left, val)
            else:
                # Then the node was found
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    replacement = self.getMinimum(root.right).val
                    root.val = replacement
                    root.right = help_remove(root.right, replacement)
            return root
        
        help_remove(self.root, val)


    def getMinimum(self, root = None) -> TreeNode:
        current = root or self.root
        while current and current.left:
            current = current.left
        return current
    

    def getMaximum(self, root = None) -> TreeNode:
        current = root or self.root
        while current and current.right:
            current = current.right
        return current
    

    def sorted(self) -> List[TreeNode]:
        "Do an in-order DFS traversal of the tree, returning the values in sorted order."
        output = []
        stack = []
        current = self.root

        while current or stack: # Iterate through the entire tree
            while current: # Go down the left until you can't
                stack.append(current)
                current = current.left
            # Once that loop breaks, we are at the bottom left
            # current is None
            current = stack.pop() # Bring us up back one; left traversal complete
            output.append(current) # Add the "current" root
            current = current.right # Now begin the right traversal
        return output 
        
        # def traverse(root):
        #     if not root:
        #         return

        #     traverse(root.left)
        #     collection.append(root.val)
        #     traverse(root.right)
        
        # collection = []
        # traverse(self.root)
        # return collection
    

    def preorder(self) -> List[TreeNode]:
        def traverse(root):
            if not root:
                return

            collection.append(root)
            traverse(root.left)
            traverse(root.right)
        
        collection = []
        traverse(self.root)
        return collection
    

    def postorder(self) -> List[TreeNode]:
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            traverse(root.right)
            collection.append(root)
        
        collection = []
        traverse(self.root)
        return collection
    

    def bylevel(self) -> List[TreeNode]:
        queue = deque()
        collection = []

        if self.root:
            queue.append(self.root)

        while queue:  # We must account for every node in the tree
            level = []
            # This second loop accounts for every level of the tree
            # At the end of a traversal of a level, the queue will only contain
            # the nodes of the next level. So we can track how many iterations
            # to do in the next level just by taking its length.
            # So even though the queue varies in size at every loop,
            # there will be a cutoff when the current level ends.
            for _ in range(len(queue)): 
                current = queue.popleft()
                level.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            collection.append(level)
        return collection
    

if __name__ == "__main__":
    tree = BinarySearchTree.fromValue(10)
    for val in [12, 11, 15, 8, 2, 3, 14, 5, 5]:
        tree.insert(val)

    # target = 12
    # print(f"Searching for {target}: {tree.search(target)}")
    # print(f"Removing {target}")

    # target = 10
    # print(f"Searching for {target}: {tree.search(target)}")

    print(tree.sorted())
    print(tree.preorder())
    print(tree.postorder())
    print(tree.bylevel())