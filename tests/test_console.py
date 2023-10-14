#!/usr/bin/python3
"""Defines a class TestHBNBCommandDocs coios dfolaoisdj for HBNBCommand class/ console"""
import unittest
import pep8
import console
from console import HBNBCommand


class TestHBNBCommandDocs(unittest.TestCase):
    """Tests for HBNBCommand sdfjos;lasdod jsdc documentation
    """

    def test_console_conforms_pep8(self):
        """Test if console.py  ijsdoa sdfokpd conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testconsole_conforms_pep8(self):
        """Test that tests/test_console.py zcisdk oidvms  conforms to PEP8 guidelines.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the moduleopfps  docstring.
        """
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for HBNBCommand skfojosclc class docstring.
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
