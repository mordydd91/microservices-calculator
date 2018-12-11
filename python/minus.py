import sys

def minus(a,b):
    return a-b

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(minus(a, b))