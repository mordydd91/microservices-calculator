'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import mult

class Minus(unittest.TestCase):
    
    def test_minus(self):
        assert(mult.mult(5, 5) == 25)
        assert(mult.mult(6, -1) == -6)
        assert(mult.mult(-1.5, 1.5) == -2.25)
        assert(mult.mult(10, 0) == 0)
        
    def test_service(self):
        assert(float(cmd.execute_microservice(5,5,"mult.py")) == 25)
        assert(float(cmd.execute_microservice(6,-1,"mult.py")) == -6)
        assert(float(cmd.execute_microservice(-1.5,1.5,"mult.py")) == -2.25)
        assert(float(cmd.execute_microservice(10,0,"mult.py")) == 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Div.testName']
    unittest.main()