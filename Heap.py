import heapq

from typing import Optional, Tuple

class MinHeap:
    """Wrapper for the python stdlib implementation of the Heap"""
    def __init__(self, iterable: list = []) -> None:
        self.heap = iterable
        heapq.heapify(self.heap)


    def __str__(self):
        return str(self.heap)
    

    def __iter__(self):
        self._index = 0
        return self


    def __next__(self):
        if self._index >= len(self.heap):
            raise StopIteration

        x = self._index
        self._index += 1
        return x, self.heap[x]

    def push(self, item: any) -> None:
        heapq.heappush(self.heap, item)


    def pop(self) -> any:
        return heapq.heappop(self.heap)
    

    def peek(self) -> any:
        try:
            return self.heap[0]
        except IndexError:
            return None


    def pushmany(self, iterable: list) -> None:
        self.heap += iterable
        heapq.heapify(self.heap)


    def _child(self, i, b) -> Optional[Tuple[int, any]]:
        j = 2*i+b
        try:
            return j, self.heap[j]
        except IndexError:
            return None


    def left(self, index: int) -> Optional[Tuple[int, any]]:
        """Return the index of the left child and the left child, or None if
        the node at the given index does not have one.
        """
        return self._child(index, 1)  # Left child formula is 2x+1
    

    def right(self, index: int) -> Optional[Tuple[int, any]]:
        """Return the index of the right child and the right child, else None"""
        return self._child(index, 2)
    

    def parent(self, index: int) -> Optional[Tuple[int, any]]:
        """Return the index of the parent node and the parent, or None if 0 is passed"""
        if index == 0:
            return None
        elif index < 0 or index > len(self.heap):
            raise ValueError
        
        j = int((index - 1) / 2)
        return j, self.heap[j]


if __name__ == "__main__":
    heap = MinHeap([2, 5, 8, 12, 3, 1, 17, 3])
    print(heap)

    heap.pushmany([3, 3, 4, 5])
    print(heap)
