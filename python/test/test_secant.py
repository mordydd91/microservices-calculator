'''
Created on Dec 16, 2018

@author: Pavel
'''
import os
import unittest
import runCmdCommand as cmd
import secant_method as sm


class Minus(unittest.TestCase):

    def test_minus(self):
        assert (sm.secant_method(lambda x:x**2, -1,1) == 0)
        assert (sm.secant_method(lambda x: x**2 -2, 0, 3) == 2)

    def test_service(self):
        assert (float(cmd.execute_microservice(1,2,"secant_method.py")) == 2**0.5)
        assert (float(cmd.execute_microservice("", "", "secant_method.py")) == 2**0.5)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()