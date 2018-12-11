def secant_method(f, x0, x1, epsilon=10**-4, nMax=100):
    n=1
    while n<=nMax:
        x2 = x1 - f(x1) * ((x1 - x0) / float(f(x1) - f(x0)))
        if (abs(f(x2))<epsilon):
            print("\nThe root is: {}".format(x2))
            return x2
        else:
            print("x0: {}, x1: {}".format(x0, x1))
            x0=x1
            x1=x2
    return False

if __name__ == "__main__":
    func = lambda x: x**2-2
    print(secant_method(func, 1, 2))