from math import log

def optimal_iteration(a, b, epsilon):
    div=epsilon/float(b-a)
    return abs(round(-1*log(div,2)-1))

def bisection_method(aX, bX, f, epsilon=10**-4):
    if(f(aX)*f(bX)>0):
        return "Error! f(a) and f(b) don't have opposite signs"
    num_iteration = optimal_iteration(aX, bX, epsilon)
    count = 0
    mX = (aX + bX) / 2.0
    while(count<num_iteration and abs(f(mX))>epsilon):
        if(f(aX)*f(mX)<0):
            bX=mX
        else:
            aX=mX
        count+=1
        mX = (aX + bX) / 2.0
    return str(mX)

if __name__ == "__main__":
    func = lambda x: x**2-2
    print(bisection_method(1,2, func))