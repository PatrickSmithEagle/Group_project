"""
File: listbag.py
Author: Man-Chi Leung
Patrick Smith
9-25-22
added definitions to the methods
"""


class ListBag(object):
    """A list-based bag implementation."""

    # Constructor
    def __init__(self, source_collection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = list()
        self.size = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    # Accessor methods
    def is_empty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ListBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        count = 0
        for i in self:
            if i == item:
                count += 1
        return count

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = list()

    def add(self, item):
        """Adds item to self."""
        if len(self) == len(self.items):
            self.items.append(None)
        self.items[len(self)] = item
        self.size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        Postcondition: item is removed from self."""
        if item not in self:
            raise KeyError(str(item) + " not in bag")
        target_index = 0
        for i in self:
            if i == item:
                break
            target_index += 1
        for i in range(target_index, len(self) - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1
