import sys

def getParam():
    argCount = len(sys.argv) - 1
    if(argCount<2) : return "not enough args, argCount=" + str(argCount) + "<2"
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        return (a, b)
    except:
        return "NaN"
