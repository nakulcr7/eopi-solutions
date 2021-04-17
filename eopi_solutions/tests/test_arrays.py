import unittest
from unittest.mock import patch


from eopi_solutions import arrays


class TestArrays(unittest.TestCase):
    def test_partition_array(self) -> None:
        self.assertListEqual(arrays.partition_array([1, 3, 2], 2), [1, 2, 3])
        self.assertListEqual(arrays.partition_array([3, 2, 1], 1), [1, 2, 3])

        # one possible version: [1, 2, 2, 3, 3, 4, 5]
        partitioned = arrays.partition_array([4, 3, 3, 5, 2, 2, 1], 2)
        self.assertTrue(all(i < 3 for i in partitioned[:3]))
        self.assertTrue(all(i == 3 for i in partitioned[3:4]))
        self.assertTrue(all(i > 3 for i in partitioned[5:]))

    def test_trade_single_stock(self) -> None:
        self.assertEqual(arrays.trade_single_stock([1, 2, 3]), 2)
        self.assertEqual(arrays.trade_single_stock([3, 2, 1]), 0)
        self.assertEqual(arrays.trade_single_stock([5, 1, 3, 2, 4, 1]), 3)
    
    def test_random_subset(self) -> None:
        self.assertEqual(arrays.random_subset([1, 2, 3], 3), [1, 2, 3])
        with patch("random.randint", side_effect=[0, 2, 4]):
            self.assertEqual(arrays.random_subset([1, 2, 3, 4, 5], 3)[:3], [1, 3, 5])

    def test_spiral_order(self) -> None:
        self.assertListEqual(arrays.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.assertListEqual(arrays.spiral_order([[1, 2], [3, 4]]), [1, 2, 4, 3])