#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import time

class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        """Test attributes of BaseModel"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_base_model_str(self):
        """Test __str__ method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_base_model_save(self):
        """Test save method of BaseModel"""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        time.sleep(1)  # Introduce a delay to ensure updated_at changes
        my_model.save()
        self.assertNotEqual(my_model.updated_at, original_updated_at)

    def test_base_model_to_dict(self):
        """Test to_dict method of BaseModel"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertIn('__class__', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('name', my_model_dict)
        self.assertIn('my_number', my_model_dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)

if __name__ == '__main__':
    unittest.main()
