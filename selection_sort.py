class SortSelection:
    """
    Sort selection algorithm | O(n^2)

    Arguments:
            arr -- some kind of array

    """

    def __init__(self, arr):
        self.arr = arr

    def find_smallest(self) -> [int, float]:
        """
        Finds and returns smallest item of array

        Returns:
            integer, float
        """

        smallest_item = self.arr[0]
        smallest_index = 0

        for i in range(len(self.arr)):
            if smallest_item > self.arr[i]:
                smallest_item = self.arr[i]
                smallest_index = i

        return smallest_index

    def sort_selection(self) -> list:
        """
        Sorts items by smallest

        Returns:
            list
        """
        newArr = []

        for i in range(len(self.arr)):
            smallest = self.find_smallest()
            newArr.append(self.arr.pop(smallest))
        return newArr

    def get_sorted(self) -> list:
        """
        Gives sorted array

        Returns:
            list
        """
        return self.sort_selection()


# * EXAMPLE
arr = [1, 5, 4, 6, 3, 2]  # test array
selection = SortSelection(arr)  # init
print(selection.get_sorted())  # result


# * RESULT
# [1, 2, 3, 4, 5, 6]
