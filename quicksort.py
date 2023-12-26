# EXERCICES
# 1. Write out the code for sum() function
# 2. Write a recursive function to count the number of items of in the list
# 3. Find the maximum number of items
# 4. Write binary search using recursion


class Quicksort:
    def __init__(self):
        self.items_count = 0

    def calculate(self, arr):
        t = 0
        for i in arr:
            t += i

        return t

    def get_items_count(self, arr):
        if not arr:
            return 0
        else:
            return 1 + self.get_items_count(arr[1:])

    def get_max(self, arr):
        return max(arr)

    def binary_search(self, arr, item, low, high):
        arr = sorted(arr)
        if high >= low:
            mid = (high + low) // 2
            guess = arr[mid]

            if guess == item:
                return mid

            elif guess > item:
                high = mid - 1
                return self.binary_search(arr, item, low, high)
            else:
                low = mid + 1
                return self.binary_search(arr, item, low, high)

        return -1

    def quick_sort(self, arr):
        if len(arr) < 2:
            return arr

        pivot = arr[0]
        greater = [i for i in arr[1:] if i > pivot]
        lower = [i for i in arr[1:] if i <= pivot]

        return self.quick_sort(lower) + [pivot] + self.quick_sort(greater)


arr = [2, 5, 54, 0, 8, 0]
print(Quicksort().get_items_count(arr))
print(Quicksort().calculate(arr))
print(Quicksort().get_max(arr))
print(Quicksort().binary_search(arr, 8, 0, len(arr) - 1))
print(Quicksort().quick_sort(arr))
