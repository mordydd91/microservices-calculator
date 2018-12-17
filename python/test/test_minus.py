'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import minus


class Minus(unittest.TestCase):

    def test_minus(self):
        self.assertEquals (minus.minus(3, 2) , 1)
        self.assertEquals (minus.minus(3, 7) , -4)
        self.assertEquals (minus.minus(1.5, -4) , 5.5)
        self.assertEquals (minus.minus(0, 0) , 0)

    def test_service(self):
        self.assertEquals (float(cmd.execute_microservice(1, 2, "minus.py")) , -1)
        self.assertEquals (float(cmd.execute_microservice(5, 3, "minus.py")) , 2)
        self.assertIn ("NaN", str(cmd.execute_microservice("rrr", "ff", "minus.py")))
        self.assertIn ("not enough args", str(cmd.execute_microservice("", 2, "minus.py")))


if __name__ == "__main__":
    unittest.main()