from getParam import getParam

def plus(a,b):
    return a+b

def service():
    param = getParam()
    if isinstance(param, str): return param
    a,b = param
    return plus(a,b)

if __name__ == "__main__":
    print(service())
