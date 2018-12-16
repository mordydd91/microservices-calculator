from getParam import getParam

def mult(a,b):
    return a*b

def service():
    param = getParam()
    if isinstance(param, str): return param
    a,b = param
    return mult(a,b)
	
if __name__ == "__main__":
    print(service())