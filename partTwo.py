import math  

def main():
    x = int(input("A"))
    y = int(input("B"))
    pythag(x,y)

def pythag(x,y):
    C = math.sqrt(x**2 + y**2)
    print (C)

main()
