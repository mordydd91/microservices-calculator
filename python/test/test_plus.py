'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import plus


class Plus(unittest.TestCase):

    def test_plus(self):
        self.assertEqual (plus.plus(1,2),3)
        self.assertEqual (plus.plus(0,0) , 0)
        self.assertEqual (plus.plus(-1,-1) , -2)

    def test_service(self):
        self.assertEqual (float(cmd.execute_microservice(1, 2, "plus.py")) , 3)
        self.assertEqual (float(cmd.execute_microservice(0, 1, "plus.py")) , 1)
        self.assertIn ("not enough args",str(cmd.execute_microservice("", "1", "plus.py")))
        self.assertIn ("NaN",str(cmd.execute_microservice("da", "1", "plus.py")))

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Div.testName']
    unittest.main()