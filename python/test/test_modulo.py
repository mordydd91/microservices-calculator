'''
Created on Dec 16, 2018

@author: Pavel
'''
import unittest
import runCmdCommand as cmd
import modulo


class Modulo(unittest.TestCase):

    def test_modulo(self):
        self.assertEquals (modulo.modulo(5,2) , 1)
        self.assertEquals (modulo.modulo(1, 0),None)
        self.assertEquals (modulo.modulo(4, 2) , 0)
        self.assertEquals (modulo.modulo(0, 0),None)

    def test_service(self):
        self.assertEquals (float(cmd.execute_microservice(11, 3, "modulo.py")) , 2)
        self.assertEquals (float(cmd.execute_microservice(5, 2, "modulo.py")) , 1)
        self.assertEquals (float(cmd.execute_microservice(1, 2, "modulo.py")) , 1)
        self.assertIn ("cannot modulo by zero", str(cmd.execute_microservice(0, 0, "modulo.py")))
        self.assertIn ("NaN" , str(cmd.execute_microservice("e", "z", "modulo.py")))


if __name__ == "__main__":
    unittest.main()