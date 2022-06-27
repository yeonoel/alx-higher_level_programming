#!/usr/bin/python3
"""Unittests for max_integer """

import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer() """

    def test_ordered_list(self):
        """Test an orded list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an ordered list of integers """
        unordered = [1, 2, 4, 5]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_begginning(self):
        """ Test a list a beginning max value"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element"""
        one_elemnt = [7]
        self.assertEqual(max_integer(one_elemnt), 7)
        
    def test_floats(self):
        """Test a list of floats"""
        floats = [1.33, 6.45, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.20, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15)

    def test_string(self):
        """Test a string"""
        string = "dance"
        self.assertEqual(max_integer(string), 'n')

    def test_list_of_string(self):
        """test a list of string"""
        string = ["Light", "is", "my", "name"]
        self.assertEqual(max_integer(string), "name")

    def test_empty_string(self):
        """test an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
