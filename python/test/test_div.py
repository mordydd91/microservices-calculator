'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import div


class Div(unittest.TestCase):

    def test_div(self):
        self.assertEquals (div.div(1,2),0.5)
        self.assertEquals (div.div(10, 2),5)
        self.assertEqual  (div.div(1, 0),None)
        self.assertEquals (div.div(0, 0),None)

    def test_service(self):
        self.assertEquals (float(cmd.execute_microservice(1, 2, "div.py")),0.5)
        self.assertEquals (float(cmd.execute_microservice(10, 2, "div.py")),5)
        self.assertIn ("cannot divide by zero",str(cmd.execute_microservice(1,0, "div.py")))
        self.assertIn("NaN",str(cmd.execute_microservice("dd", "ddd", "div.py")))


if __name__ == "__main__":
    unittest.main()