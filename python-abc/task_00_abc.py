#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        """ Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        """ Return the sound made by a dog."""
        return "Meow"
