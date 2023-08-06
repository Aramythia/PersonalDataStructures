CAPACITY = 1000

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None


class ChainedHashSet:
    """HashSet that uses the Chaining method for handling collisions"""
    def __init__(self) -> None:
        self.capacity = CAPACITY
        self.array = [[] for _ in range(self.capacity)]
        self.size = 0


    def __len__(self) -> int:
        return self.size
    

    def __str__(self) -> str:
        keys = []
        for lst in self.array:
            keys += lst
        return "{" + ', '.join([str(k) for k in keys]) + "}"
    

    def __repr__(self) -> str:
        return self.__str__()


    def __contains__(self, key) -> int:
        index = self._hash(key)
        return key in self.array[index]

    
    def _hash(self, key) -> int:
        return key % self.capacity
    

    def put(self, key):
        index = self._hash(key)
        if key in self.array[index]:
            return
        else:
            self.array[index].append(key)
            self.size += 1


    def remove(self, key):
        index = self._hash(key)
        if key in self.array[index]:
            self.array[index].remove(key)
            self.size -= 1


class ChainedHashMap:
    def __init__(self) -> None:
        self.capacity = CAPACITY
        self.array = [Node(-1, -1) for _ in range(self.capacity)]
        self.size = 0


    def __len__(self) -> int:
        return self.size
    

    def __str__(self) -> str:
        keys = []
        for lst in self.array:
            current = lst  # Gets the dummy head
            while current.next is not None:
                keys.append(f"{current.next.key}: {current.next.val}")
                current = current.next

        return "{" + ', '.join(keys) + "}"
    

    def __repr__(self) -> str:
        return self.__str__()


    def __contains__(self, key) -> int:
        try:
            self.get(key)
        except KeyError:
            return False
        else:
            return True
        

    def __getitem__(self, key):
        return self.get(key)
    

    def __setitem__(self, key, value):
        return self.put(key, value)
    

    def __delitem__(self, key):
        return self.remove(key)

    
    def _hash(self, key) -> int:
        return key % self.capacity
    

    def put(self, key, val):
        index = self._hash(key)
        current = self.array[index]

        # Find the node with the key in the LinkedList
        while current.next is not None:
            if current.next.key == key:
                current.next.val = val
                return
            else:
                current = current.next

        # Otherwise add it to the end
        current.next = Node(key, val)
        self.size += 1


    def get(self, key):
        index = self._hash(key)
        current = self.array[index]

        # Find the node with the key in the LinkedList
        while current.next is not None:
            if current.next.key == key:
                return current.next.val
            else:
                current = current.next

        # Otherwise its not in the list
        raise KeyError
    
    
    def remove(self, key):
        index = self._hash(key)
        current = self.array[index]

        # Find the node with the key in the LinkedList
        while current.next is not None:
            if current.next.key == key:
                current.next = current.next.next
                self.size -= 1
                return
            else:
                current = current.next


if __name__ == "__main__":
    # x = ChainedHashSet()
    # for n in (4, 6, 123, 34, 19, 903434, 6, 2, 6, 16, 1000, 2000):
    #     x.put(n)
    #     print(x)
    # print(6 in x)

    y = ChainedHashMap()
    for k, v in [(2, 1), (9, 19), (1009, 6), (9, 14), (3, 3)]:
        y[k] = v
        print(y)
    print(len(y))
    print(3 in y, 5 in y)