class BinarySearch:
    def __init__(self, list) -> int:
        self.list = list
        self.iteration_count = 0

    def find_item(self, item):
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
        return self.iteration_count


search = BinarySearch([1, 3, 5, 6, 7, 9])  # set up list

print(search.find_item(3))  # search item
print(search.get_iteration_count())  # count how many times iteration works
