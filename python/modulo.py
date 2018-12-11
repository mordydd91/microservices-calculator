import sys

def modulo(a,b):
    if(b is not 0):
        return a%b

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(modulo(a, b))