#!/usr/bin/env python3
class CountedIterator:
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
            self.counter += 1
            return next(self.iterator)
        except StopIteration:
            raise
