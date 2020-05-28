import unittest
from interfaceTest import excellist
import  paramunittest


#调用读取excel的方法
querylist=excellist.test_something('O2O')
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
