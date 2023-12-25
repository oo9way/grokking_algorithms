# RECURSION
# You're digging through your grandma's attic and come across a mysterious locked suitcase.
# Grandma tells you that the key for the suitcase is probably in this other box.
# This box contains more boxes, with more boxes inside those boxes. The key is in a box somewhere.
# What's your algorithm to search for the key?


class Box:
    """
    Data structure for Recursion
    """

    def __init__(self, is_key=False, id=1) -> dict:
        """

        Keyword Arguments:
            is_key -- _description_ (default: {False})
            id -- _description_ (default: {0})

        Returns:
            _description_
        """
        self.boxes = []
        self.is_key = is_key
        self.id = id

    # Get a box inside current box
    def get_inside_box(self):
        return self.boxes[0] if len(self.boxes) > 0 else None

    # Add a box to current box
    def add_box(self, is_key=False, box_id=0):
        """
        Adds a box to the current box

        Keyword Arguments:
            is_key -- set true if key in this box (default: {False})
            box_id -- give some id (0,1,2,3,4,5) (default: {0})

        Returns:
            New box object
        """

        new_box = Box(is_key=is_key, id=box_id)
        self.boxes.append(new_box)
        return new_box

    def __str__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "is_key": self.is_key,
            "box": self.boxes[0] if len(self.boxes) > 0 else None,
        }


grandpa = Box()  # Box 1
parent = grandpa.add_box(box_id=2)  # Box 2
child = parent.add_box(is_key=True, box_id=3)  # Box 3. Alos, key box.


def look_for_key(box):
    """
    Looks for a key

    Arguments:
        box -- _description_

    Returns:
        True or False
    """

    if box.is_key:
        return True, box.id

    if box.get_inside_box():
        return look_for_key(box.get_inside_box())

    return False


# RESULT --> (True, 3)


################################

# RECURSION
# EXAMPLE 2


def reverse_count(i):
    print(i)

    if i > 0:
        reverse_count(i - 1)
    else:
        return


# RESULT
# 5
# 4
# 3
# 2
# 1
# 0


################################

# RECURSION
# EXAMPLE 3


def get_factorial(x):
    if x == 1:
        return 1
    return x * get_factorial(x - 1)


print(get_factorial(5))

# RESULT --> 120
