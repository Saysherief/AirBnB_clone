#!/usr/bin/python3
"""Test cases for BaseModel class"""
import unittest
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel"""

    def test_init(self):
        """Test BaseModel init"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test BaseModel str"""
        model = BaseModel()
        model_str = str(model)
        self.assertIsInstance(model_str, str)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("id", model_str)
        self.assertIn("created_at", model_str)
        self.assertIn("updated_at", model_str)

    def test_save(self):
        """Test BaseModel save"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test BaseModel to_dict"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)


if __name__ == '__main__':
    unittest.main()
