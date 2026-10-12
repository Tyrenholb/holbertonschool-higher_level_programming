#!/usr/bin/env python3
"""Serialize and deserialize custom objects using pickle."""


import pickle
import json


class CustomObject:
    """Represent a person with a name, age, and student status."""
    def __init__(self, name, age, is_student):
        """Initialize the person's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's name, age, and student status."""
        print("Name: {}\nAge: {}\nIs Student: {}".format
              (self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Save the object to a pickle file, returning None on failure."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an object from a pickle file, or None on failure."""
        try:
            with open(filename, "rb") as f:
                restored_data = pickle.load(f)
            return (restored_data)
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
