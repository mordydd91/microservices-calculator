'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import secant_method as sm

epsilon = 0.0001
class Secant(unittest.TestCase):

    def test_secant_method(self):
        self.assertAlmostEqual (sm.secant_method(lambda x:-x**2 +1, 0,2, epsilon), 1, delta=epsilon)
        self.assertAlmostEqual (sm.secant_method(lambda x: x**2 -2, 0, 3, epsilon), 2**0.5, delta=epsilon)

    def test_service(self):
        self.assertAlmostEqual (float(cmd.execute_microservice(1,2,"secant_method.py")) , 2**0.5, delta = epsilon)
        self.assertAlmostEqual (float(cmd.execute_microservice("", "", "secant_method.py")) , 2**0.5 ,delta = epsilon)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()