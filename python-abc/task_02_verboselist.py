#!/usr/bin/env python3
class VerboseList(list):
    """
    A list subclass that prints informative messages when modified.
    """

    def append(self, item):
        """Append an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable,
        and print how many items were added."""
        items = list(iterable)
        count = len(list(iterable))
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a message.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    # define the pop() function with default index -1
    def pop(self, index=-1):
        """
        Remove and return the item at the given position in the list.
        If no index is specified, removes and returns the last item.
        """
        # get the item at the specific index in the current
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        # the argument of pop() must be an index, not a item value
        return super().pop(index)


"""
the original list.pop() does two things:
- remove the item at given index;
- return the value that was removed
"""
