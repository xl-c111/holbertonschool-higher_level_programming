#!/usr/bin/env python3
class SwimMixin:
    """Mixin class that adds swimming ability to a creature."""

    def swim(self):
        """ Print a message indicating that the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that adds flying ability to a creature."""

    def fly(self):
        """ Print a message indicating that the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon that can swim and fly,
    by inheriting from SwimMixin and FlyMixin.
    """

    def roar(self):
        """ Print a message indicating that the dragon roars."""
        print("The dragon roars!")


draco = Dragon()
