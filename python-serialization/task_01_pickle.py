#!/usr/bin/python3
"""This module defines the CustomObject class, which supports pickling-based
serialization and deserialization of its instances."""
import pickle


class CustomObject:
    """A custom class that can be serialized to and deserialized from a file
    using pickle"""

    def __init__(self, name, age, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("name: {}".format(self.name))
        print("age: {}".format(self.age))
        print("is_student: {}".format(self.is_student))

    def serialize(self, filename):
        with open(filename, "wb") as f:
            return pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)

        # when deserialize from an empty, missing or corrupted file, python
        # will raise exceptions to avoid crushing
        except (EOFError, pickle.UnpicklingError, FileNotFoundError) as e:
            print(f"Failed to deserialize from {filename}: {e}")
            return None
