from runCmdCommand import execute_microservice
from getParam import getParam

plus = "plus.py"
minus = "minus.py"

def mult(a,b):
	c=0
	if(b<0):
		a=float(execute_microservice(0,a,minus))
		b=float(execute_microservice(0,b,minus))
	for _ in range(int(b)):
		c=float(execute_microservice(c,a,plus))
	return c

def service():
	param = getParam()
	if isinstance(param, str): return param
	a,b = param
	if(abs(float(execute_microservice(b,int(b),minus)))>0):
		return "<b> not Integer"
	return mult(a,b)

if __name__ == "__main__":
	print(service())
