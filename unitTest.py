import unittest
from calculator import Calculator

class calculatorTest(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator(3,4)

    def test_0_add(self):
        self.value = self.cal.add()
        self.ans=2
        self.assertEqual(self.value,self.ans)

    def test_1_sub(self):
        self.value = self.cal.sub()
        self.ans=-1
        self.assertEqual(self.value,self.ans)

    def test_2_mul(self):
        self.value = self.cal.mul()
        self.ans=12
        self.assertEqual(self.value,self.ans)

    def test_3_div(self):
        self.value = self.cal.div()
        self.ans=round(3/4,2)
        self.assertEqual(self.value,self.ans)



if __name__ == '__main__':
    unittest.main()
