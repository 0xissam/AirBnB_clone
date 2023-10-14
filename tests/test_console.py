#!/usr/bin/python3

import pep8
import unittest
from console import HBNBCommand
import console



class TestHBNBCommandDocs(unittest.TestCase):

    def test_console_conforms_pep8(self):
        
        
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testconsole_conforms_pep8(self):
        
        
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        
        
        self.assertTrue(len(console.__doc__) >= 1)

    def test_class_docstr(self):
        
        
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)
