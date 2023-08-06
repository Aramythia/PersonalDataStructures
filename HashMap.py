CAPACITY = 1000

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


    def remove(self, key):
        index = self._hash(key)
        if key in self.array[index]:
            self.array[index].remove(key)


if __name__ == "__main__":
    x = ChainedHashSet()
    for n in (4, 6, 123, 34, 19, 903434, 6, 2, 6, 16, 1000, 2000):
        x.put(n)
        print(x)
    print(6 in x)