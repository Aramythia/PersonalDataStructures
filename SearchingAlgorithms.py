import random


def binary_search(arr: list, target: int) -> int:
    """Use the Binary Search Algorithm - O(logn)"""
    left, right = 0, len(arr)-1

    while left <= right:
        midpoint = int((left + right) / 2)

        if target > arr[midpoint]:
            left = midpoint+1
        elif target < arr[midpoint]:
            right = midpoint-1
        else:
            return midpoint
        
    raise ValueError(f"Target {target} not in array.")


if __name__ == "__main__":
    arr = [random.randint(1, 10) for _ in range(10)]
    arr.sort()
    target = random.randint(1, 10)

    print(f"Searching for [{target}] in {arr}...")
    try:
        index = binary_search(arr, target)
        print(f"Target found at index {index}.")
    except ValueError as e:
        print(e)