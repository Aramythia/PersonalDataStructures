import random

def merge_sort(arr: list) -> None:
    """Use the Merge Sort Algorithm - Stable O(nlogn) time and O(n) space"""
    def merge(arr, s, m, e):
        # Copy the sorted left & right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0 # index for L
        j = 0 # index for R
        k = s # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(arr, start, end):
        # Base Case: array length is 1
        if end-start+1 <= 1:
            return

        # Split the array in half and sort them
        midpoint = int((start + end) / 2)
        sort(arr, start, midpoint)
        sort(arr, midpoint+1, end)

        # Merge the two arrays
        merge(arr, start, midpoint, end)

        return

    sort(arr, 0, len(arr))


def quick_sort(arr: list) -> None:
    """Use the QuickSort Algorithm - Unstable O(nlogn) time and O(1) space"""
    def sort(arr, start, end):
        # Base Case: array length is 1
        if end-start+1 <= 1:
            return arr
        
        pivot = arr[end-1] # Select a pivot (this can be optimized)
        # The pivot is a value to which every other element will be compared
        # Elements less than the pivot will be placed on the left side of
        # the list, else they will go right. That way the list can be split
        # into 2 relatively sorted partitions, ready for a recursive call
        partition = start
        for i in range(start, end):
            if arr[i] < pivot:
                arr[partition], arr[i] = arr[i], arr[partition]
                partition += 1

        # Put the pivot variable in the middle - it is in sorted position
        arr[partition], arr[end-1] = arr[end-1], arr[partition]

        # Sort the two partitions around the pivot
        sort(arr, start, partition)
        sort(arr, partition+1, end)

    sort(arr, 0, len(arr))

def bucket_sort(arr: list) -> list:
    """Use the BucketSort Algorithm - Unstable O(nlogn) time and O(n) space"""
    # Get the bounds of our bucket array
    minimum, maximum = arr[0], arr[0]
    for element in arr:
        if element < minimum:
            minimum = element
        elif element > maximum:
            maximum = element

    buckets = [0]*(maximum - minimum + 1)

    # Fill the bucket
    for element in arr:
        buckets[element - minimum] += 1

    # Return the array
    result = []
    for i, val in enumerate(buckets):
        result += ([i + minimum]*val)
    return result


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]

    print("Sorting array", arr, "-> ", end="")

    # merge_sort(arr)
    # quick_sort(arr)
    arr = bucket_sort(arr)

    print(arr)