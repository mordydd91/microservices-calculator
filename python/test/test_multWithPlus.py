'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import multWithPlus

class MultWithPlus(unittest.TestCase):
    
    def test_mult(self):
        self.assertEqual(multWithPlus.mult(5, 5) , 25)
        self.assertEqual(multWithPlus.mult(6, -1) , -6)
        self.assertNotEqual(multWithPlus.mult(-1.5, 1.5) , -2.25)
        self.assertEqual(multWithPlus.mult(10, 0) , 0)
        self.assertEqual(multWithPlus.mult(-10, 3) , -30)
        
    def test_service(self):
        self.assertEqual(float(cmd.execute_microservice(5,5,"multWithPlus.py")) , 25)
        self.assertEqual(float(cmd.execute_microservice(6,-1,"multWithPlus.py")) , -6)
        self.assertIn("<b> not Integer",str(cmd.execute_microservice(-1.5,1.5,"multWithPlus.py")))
        self.assertEqual(float(cmd.execute_microservice(10,0,"multWithPlus.py")) , 0)
        self.assertEqual(float(cmd.execute_microservice(-10.5,3,"multWithPlus.py")) , -31.5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Div.testName']
    unittest.main()