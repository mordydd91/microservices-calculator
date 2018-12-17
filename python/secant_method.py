import runCmdCommand as cmd

minusService = r"minus.py" 

def secant_method(f, x0, x1, epsilon=10**-4, nMax=100):
    n=1
    while n<=nMax:
        temp1 = float(cmd.execute_microservice(f(x1), f(x0), minusService))
        x2 = x1 - f(x1) * ((x1 - x0) / temp1)
        if (abs(f(x2))<epsilon):
            return x2
        else:
            x0=x1
            x1=x2
    return False

if __name__ == "__main__":
    func = lambda x: x**2-2
    print(secant_method(func, 1, 2))