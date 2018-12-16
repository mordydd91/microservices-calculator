from getParam import getParam

def div(a,b):
    if(b is not 0):
        return a/b

def service():
    param = getParam()
    if isinstance(param, str): return param
    a,b = param
    if(b==0): return "cannot devide by zero"
    return div(a,b)
	
if __name__ == "__main__":
    print(service())