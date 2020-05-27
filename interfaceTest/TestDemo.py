import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("------start----------")
    def tearDown(self):
        print("----------end--------------")
    def test1(self):
        print("测试用例1")
    def test2(self):
        print("测试用例2")

if __name__ == '__main__':
    unittest.main()
