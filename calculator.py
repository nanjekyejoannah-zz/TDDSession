import unittest

class Calculator():

    def addme(self,num1,num2):

    	result  = num1 + num2
        return result

    def multplyme(self,num1,num2):

    	result  = num1 * num2
        return result

    def subtract(self,num1,num2):

    	result  = num1-num2
        return result

    def divide(self,num1,num2):

    	result  = num1/num2
        return result



class calculatortest(unittest.TestCase):

    def test_add(self):
        clc = Calculator()
        result = clc.addme(3,2)
        self.assertEqual(5, result)

    def test_multiply(self):
        clc = Calculator()
        result = clc.multplyme(3,2)
        self.assertEqual(6, result)

    def test_subtract(self):
        clc = Calculator()
        result = clc.subtract(3,2)
        self.assertEqual(1, result)

    def test_divide(self):
        clc = Calculator()
        result = clc.divide(4,2)
        self.assertEqual(2, result)


suite = unittest.TestLoader().loadTestsFromTestCase(calculatortest)
unittest.TextTestRunner(verbosity=2).run(suite)
