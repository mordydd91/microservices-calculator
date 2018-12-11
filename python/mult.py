import sys

def mult(a,b):
    return a*b

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(mult(a, b))