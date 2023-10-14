#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
import datetime
from models.state import State



class TestState(unittest.TestCase):
    

    @classmethod
    def setUp(cls):
        
        
        cls.state1 = State()
        cls.state1.name = "Nairobi"

    @classmethod
    def tearDown(cls):
        
        
        del cls.state1

    def test_class_exists(self):
        
        
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state1)), result)

    def test_inheritance(self):
        
        
        self.assertIsInstance(self.state1, State)
        self.assertEqual(type(self.state1), State)
        self.assertEqual(issubclass(self.state1.__class__, BaseModel), True)

    def test_types(self):
        
        
        self.assertIsInstance(self.state1.id, str)
        self.assertEqual(type(self.state1.id), str)
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)
        self.assertIsInstance(self.state1.name, str)

    def test_save(self):
        
        
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_functions(self):
        
        
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        
        
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))
        self.assertTrue(hasattr(self.state1, 'name'))

    def test_to_dict(self):
        
        
        my_model_json = self.state1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.state1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.state1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.state1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.state1.id)

    def test_unique_id(self):
        
        
        state2 = self.state1.__class__()
        state3 = self.state1.__class__()
        state4 = self.state1.__class__()
        self.assertNotEqual(self.state1.id, state2.id)
        self.assertNotEqual(self.state1.id, state3.id)
        self.assertNotEqual(self.state1.id, state4.id)


if __name__ == '__main__':
    unittest.main()
