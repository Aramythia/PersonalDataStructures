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



if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]

    print("Sorting array", arr, "-> ", end="")

    merge_sort(arr)

    print(arr)