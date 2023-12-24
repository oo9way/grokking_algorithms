class BinarySearch:
    """
     Binary search algorithm | O(log n)

    Arguments:
        arr -- some kind of array
    """

    def __init__(self, list) -> int:
        self.list = list
        self.iteration_count = 0

    def find_item(self, item) -> [int, None]:
        """
        Finds given item from list using binary search

        Arguments:
            item -- int, float, str

        Returns:
            int - index of found item
            None - when item is not found
        """

        low = 0
        high = len(self.list) - 1

        while low <= high:
            self.iteration_count += 1
            mid = (low + high) // 2
            guess = self.list[mid]

            if guess == item:
                return mid

            if guess > item:
                high = mid - 1

            else:
                low = mid + 1

        return None

    def get_iteration_count(self) -> int:
        """
        Get how many times iterated to search item

        Returns:
            int - count of iteration
        """

        return self.iteration_count


# * EXAMPLE
search = BinarySearch([1, 3, 5, 6, 7, 9])  # set up list

print("Found item index ", search.find_item(3))  # search item
print("Iteration counter", search.get_iteration_count())  # count iterations


# * RESULT
# Found item index  1
# Iteration counter 3
