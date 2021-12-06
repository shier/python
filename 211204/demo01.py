"""
calc area of cir
"""
PI = 3.1415926
def input_number():
    #input a number
    while True:
        r = input("Please input Radio:")
        try:
            r = float(r)
            return r
        except:
            print("not correct input")

def get_Area(x:float):

    return x*x*PI

def get_primeter(x:float):

    return 2*PI*x

if __name__ == '__main__':
    r = input_number()
    primeter_num = get_primeter(r)
    print(primeter_num)
