#!/usr/bin/python3
"""Define test cases for the User class."""
import unittest
from models.user import User
import os
import models
from datetime import datetime


class TestUser(unittest.TestCase):
    """Define test cases for the User class."""

    def test_attribute_types(self):
        """Test that the attribute types are correct."""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_attribute_values(self):
        """Test that the attribute values are correct."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test that User class inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_str_representation(self):
        """Test the __str__ method of the User class."""
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        expected = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(expected, str(user))
