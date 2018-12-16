from getParam import getParam

def modulo(a,b):
    if(b is not 0):
        return a%b

def service():
    param = getParam()
    if isinstance(param, str): return param
    a,b = param
    if(b==0): return "cannot modulo by zero"
    return modulo(a,b)
	
if __name__ == "__main__":
    print(service())