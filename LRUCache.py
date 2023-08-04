"""
How do you make an LRU cache have O(1) in all its operations?

Only 1 data structure has O(1) for all its operations - the dict.
Retrieval is easily O(1), but finding what to remove is going to require a
    loop - O(n). We need a data structure that keeps track of the max timestamp.
Heap insertion is O(logn), so the timestamp idea is out.
What we can use instead of timestamps is maintain a queue to log operations.
    Whichever node is at the head of the queue is the most recently used
Problem: But if a node has multiple operations, there's no way to track
    its operations that have been enqueued.
Solution: So instead of using a queue, we go bare-bones and just take a 
    Linked List, which lets use remove from the middle.
Problem: But linked lists don't have random access
Solution: have the dict track the linked list nodes

Doubly Linked List head: least recently used
Doubly Linked List tail: most recently used
Dictionary tracks all list nodes for modification

REMEMBER: LRU WITH DICTIONARY AND DOUBLY LINKED LIST
"""

class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

    def __str__(self) -> str:
        return f"({self.key}: {self.val})"
    
    def __repr__(self) -> str:
        return self.__str__()
    

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}  # Keep track of all nodes for random access

        # REMEMBER to always have dummy nodes to handle edge cases
        # To get the actual LRU and MRU, take the neighbors of these dummies
        self.lru, self.mru = Node(-1, -1), Node(-1, -1)
        self.lru.next = self.mru
        self.mru.prev = self.lru


    def __str__(self) -> str:
        return f"{self.cache}; LRU: {self.lru.next}"
    

    def __repr__(self) -> str:
        return self.__str__()


    def _remove(self, node: Node):
        """Helper function to remove a node from our linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev


    def _insert(self, node: Node):
        """Add node at MRU position (it was just used)"""
        node.next = self.mru
        node.prev = self.mru.prev
        self.mru.prev = node
        node.prev.next = node


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]  # Random Access for our node

            # Take it from the queue and put it as the MRU
            self._remove(node)
            self._insert(node)

            return node.val
        else:
            return -1

    def put(self, key, value):
        node = Node(key, value)
        if key in self.cache:  # Solves problem with queue -> just take it out
            self._remove(self.cache[key])

        self.cache[key] = node
        self._insert(node)

        # Make sure we remain at capacity
        if len(self.cache) > self.capacity:
            lru = self.lru.next  # self.lru is the dummy, its .next is the actual LRU
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    x = LRUCache(2)

    for operation in ((1, 1), (1,), (2, 2), (1, 3), (3, 3), (4, 4), (3,)):
        if len(operation) == 1:
            print(f"Getting value for {operation[0]}: ", end="")
            print(x.get(operation[0]))
        else:
            print(f"Adding", operation[0], operation[1])
            x.put(operation[0], operation[1])
            print(x)