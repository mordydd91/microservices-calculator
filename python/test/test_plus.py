'''
Created on Dec 16, 2018

@author: Pavel
'''
import os
import unittest
import runCmdCommand as cmd
import plus


class Minus(unittest.TestCase):

    def test_minus(self):
        assert (plus.plus(1,2)==3)
        assert (plus.plus("", 3) == "NaN")
        assert (plus.plus(0,0) == 0)
        assert (plus.plus(-1,-1) == -2)


    def test_service(self):
        assert (float(cmd.execute_microservice(1, 2, "plus.py")) == 3)
        assert (float(cmd.execute_microservice(0, 1, "plus.py")) == 1)
        assert (float(cmd.execute_microservice("", "1", "plus.py")) == "NaN")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()