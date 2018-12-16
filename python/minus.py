from getParam import getParam

def minus(a,b):
    return a-b

def service():
    param = getParam()
    if isinstance(param, str): return param
    a,b = param
    return minus(a,b)
	
if __name__ == "__main__":
    print(service())