import unittest

from solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()


    def test_case_1(self):
        arr = [1,2,3,4,5,6,7]
        expected = [1,7]

        self.assertEqual(self.sol.getMinMax(arr),expected)

if __name__ == '__main__':
    unittest.main()
