import unittest

from eopi_solutions import arrays


class TestArrays(unittest.TestCase):
    def test_hello_world(self) -> None:
        self.assertEqual(arrays.hello_world(), "hello, world")
