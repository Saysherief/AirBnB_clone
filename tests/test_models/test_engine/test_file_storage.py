#!/usr/bin/python3
"""Test cases for FileStorage class"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = storage
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test FileStorage all"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(self.model.__class__.__name__ + '.' + self.model.id, all_objs)

    def test_new(self):
        """Test FileStorage new"""
        model = BaseModel()
        self.storage.new(model)
        key = model.__class__.__name__ + '.' + model.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test FileStorage save"""
        self.storage.save()
        with open("file.json", mode="r") as myfile:
            self.assertIn(self.model.__class__.__name__ + '.' + self.model.id, myfile.read())

    def test_reload(self):
        """Test FileStorage reload"""
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(self.model.__class__.__name__ + '.' + self.model.id, all_objs)

if __name__ == '__main__':
    unittest.main()
