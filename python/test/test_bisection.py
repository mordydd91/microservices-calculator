'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import bisection_method as bm

epsilon = 0.0001
class Bisection(unittest.TestCase):
    def test_bisection_method(self):
        self.assertIn ("Error! f(a) and f(b) don't have opposite signs",bm.bisection_method(-1, 1, lambda x:x**2, epsilon))   #f(1)=f(-1)>0
        self.assertAlmostEqual (float(bm.bisection_method(-0.5, 1, lambda x:-x**2 +1)), 1 , delta = epsilon)
        self.assertAlmostEqual (float(bm.bisection_method(1, 2, lambda x: x**2 -2)), 2**0.5 , delta = epsilon)

    def test_service(self):
        self.assertAlmostEqual(float(cmd.execute_microservice(1,2,"bisection_method.py")), 2 ** 0.5, delta = epsilon)
        self.assertAlmostEqual(float(cmd.execute_microservice("", "2", "bisection_method.py")) , 2 ** 0.5, delta = epsilon)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()