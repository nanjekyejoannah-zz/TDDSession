import unittest
import sys

sys.path.append('/home/patricia/calculator/calc')
from calculator import  Calculator

class Calculator_test(unittest.TestCase):
    def test_add(self):
        ourclass = Calculator()
        result = ourclass.add(5,6)
        self.assertEqual(11,result)

    def test_lator(self):
        ourclass = Calculator()
        result = ourclass.add(5,6)
        self.assertEqual(4,result)

    def test_multiply(self):
        myclass = Calculator()
        ans = myclass.multiply(3,3)
        self.assertEqual(9,ans)

    def test_subtraction(self):
        yoclass = Calculator()
        sss = yoclass.subtraction(3,2)
        self.assertEqual(2,sss)

    def test_divide(self):
        theclass = Calculator()
        res = theclass.divide(4,4)
        self.assertEqual(1,res)        

suite = unittest.TestLoader().loadTestsFromTestCase(Calculator_test)
unittest.TextTestRunner(verbosity = 8).run(suite)
