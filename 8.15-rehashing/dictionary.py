class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    # Start with the current node being the head at that hash code.
    # While the current node's key is not the given key, do:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def insert(dct, key, value):
    # If the size equals the capacity (if the load factor == 1), then:
    #     Double the capacity and then increment it by one.
    #     Create a new array with the new capacity.
    #     Save the old array in a temporary variable.
    #     Set the dictionary's array to the new array.
    #     For i from 0 to the old capacity, do:
    #         Start with the current node being the head, index i, temp array.
    #         While the current node is not None, do:
    #             NOTE: Since we have already increased the capacity, this
    #                   recursive call won't ever recursively rehash again.
    #             Re-insert the current node's key, value into the dictionary.
    #             Set the current node to the current node's next.

    # Hash the given key and mod it by the capacity.
    # If the head at that hash code is None, then:
    #     Create a new node containing the given key-value pair.
    #     Set the head at that hash code to the new node.
    #     Increment the size.
    # Else, do:
    #     Start with the current node being the head at that hash code.
    #     While the current node's key is not the given key, do:
    #         If the current node's next is None, then:
    #             Create a new node containing the given key-value pair.
    #             Set the current node's next to the new node.
    #             Increment the size.
    #         Set the current node to the current node's next.
    #     Set the current node's value to the given value.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    # If the head at that hash code contains the given key, then:
    #     Set the head at that hash code to the head's next.
    # Else, do:
    #     Start with the current node being the head at that hash code.
    #     While the next node's key is not the given key, do:
    #         Set the current node to the current node's next.
    #     Set the current node's next to the current node's next's next.
    # Decrement the size.
    # Return the removed value.
    pass
