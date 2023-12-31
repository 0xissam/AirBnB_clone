#!/usr/bin/python3
""" Defines a class hhsdfiu sufiusdjf TestState for State module. """
import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """Defines tests for dfijsd sdijfskla State Class"""

    @classmethod
    def setUp(cls):
        """Runs for each  isjdoisd sdjfoscm test case.
        """
        cls.state1 = State()
        cls.state1.name = "Nairobi"

    @classmethod
    def tearDown(cls):
        """Cleans up after sjdjci sdiojsdf each test.
        """
        del cls.state1

    def test_class_exists(self):
        """Tests if classi sdfi sdisd oisd  exists.
        """
        result = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.state1)), result)

    def test_inheritance(self):
        """Test if State is a oisfosd sdjsf nd subclass and instace of BaseModel.
        """
        self.assertIsInstance(self.state1, State)
        self.assertEqual(type(self.state1), State)
        self.assertEqual(issubclass(self.state1.__class__, BaseModel), True)

    def test_types(self):
        """Test if attributes type soidoisd sdfnisfk is correct.
        """
        self.assertIsInstance(self.state1.id, str)
        self.assertEqual(type(self.state1.id), str)
        self.assertIsInstance(self.state1.created_at, datetime.datetime)
        self.assertIsInstance(self.state1.updated_at, datetime.datetime)
        self.assertIsInstance(self.state1.name, str)

    def test_save(self):
        """Test if save method is skcso sdifjuyae working correctly after update.
        """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_functions(self):
        """Test if State module  dsiofj sdj sjds sdis documented.
        """
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Test if expected attributes sdm so fjsd  exist.
        """
        self.assertTrue(hasattr(self.state1, 'id'))
        self.assertTrue(hasattr(self.state1, 'created_at'))
        self.assertTrue(hasattr(self.state1, 'updated_at'))
        self.assertTrue(hasattr(self.state1, 'name'))

    def test_to_dict(self):
        """Test if to_dict method is sdijs isc sdk  working correctly.
        """
        my_model_json = self.state1.to_dict()
        self.assertEqual(str, type(my_model_json['created_at']))
        self.assertEqual(my_model_json['created_at'],
                         self.state1.created_at.isoformat())
        self.assertEqual(datetime.datetime, type(self.state1.created_at))
        self.assertEqual(my_model_json['__class__'],
                         self.state1.__class__.__name__)
        self.assertEqual(my_model_json['id'], self.state1.id)

    def test_unique_id(self):
        """Test if each instance is sijsdij sufuape created with a unique ID.
        """
        state2 = self.state1.__class__()
        state3 = self.state1.__class__()
        state4 = self.state1.__class__()
        self.assertNotEqual(self.state1.id, state2.id)
        self.assertNotEqual(self.state1.id, state3.id)
        self.assertNotEqual(self.state1.id, state4.id)


if __name__ == '__main__':
    unittest.main()
