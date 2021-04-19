#!/usr/bin/env python3
import unittest

from eopi_solutions import strings


class TestStrings(unittest.TestCase):
    def test_int_to_str(self) -> None:
        self.assertEqual(strings.int_to_str(123), "123")
        self.assertEqual(strings.int_to_str(0), "0")
        self.assertEqual(strings.int_to_str(-123), "-123")
    
    def test_str_to_int(self) -> None:
        self.assertEqual(strings.str_to_int("123"), 123)
        self.assertEqual(strings.str_to_int("0"), 0)
        self.assertEqual(strings.str_to_int("-123"), -123)
    
    def test_base_conversion(self) -> None:
        self.assertEqual(strings.base_conversion("615", 7, 13), "1A7")
        self.assertEqual(strings.base_conversion("-615", 7, 13), "-1A7")
    
    def test_replace_and_remove(self) -> None:
        self.assertListEqual(strings.replace_and_remove(["a", "c", "d", "b", "b", "c", "a"], 7), ["d", "d", "c", "d", "c", "d", "d"])
        self.assertListEqual(strings.replace_and_remove(["x", "y", "z"], 3), ["x", "y", "z"])
        self.assertListEqual(strings.replace_and_remove(["a", "b", "a", "c", None], 4), ["d", "d", "d", "d", "c"])
        self.assertListEqual(strings.replace_and_remove(["a", "a", None, None], 2), ["d", "d", "d", "d"])