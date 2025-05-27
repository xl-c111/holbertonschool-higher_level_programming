#!/usr/bin/env python3
class CountedIterator:
    """An iterator wrapper that counts how many items have been iterated."""

    def __init__(self, iterator, counter=0):
        """
        Initialize the CountedIterator with an iterator and an optional counter
        """
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.counter

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.
        Raises StopIteration when the iterator is exhausted.
        """
        try:
            item = next(self.iterator)
            # move self.counter += 1 after successfully retrieving the next
            # item to ensure the count matches the actual number of items
            self.counter += 1
            return item
        except StopIteration:
            # break is only valid inside a loop， does not signal to outside
            # code that the ietration should stop
            raise
