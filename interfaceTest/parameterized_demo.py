import unittest
from parameterized import parameterized
import logging


class TestAdd(unittest.TestCase):
    @parameterized.expand([('01', 2, 2), ('02', 2, 2), ('03', 3, 3), ('04', 5, 5), ('05', 4, 4), ])
    def test_add(self, name, a, b):
        self.assertEqual(a, b)
        print(name, a + b)


if __name__ == '__main__':
    unittest.main()
