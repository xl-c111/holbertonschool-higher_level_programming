#!/usr/bin/env python3
class Fish:
    """A class representing a fish."""

    def swim(self):
        """Print how the fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Print how the bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, inheriting from both Fish and Bird.
    """

    def fly(self):
        """Print how the flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print how the flying fish swims."""
        print("The flying fish is swimming!")

    def habitat(self):
        """ Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
