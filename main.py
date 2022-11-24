def Quadratic():
    d = (b**2) - (4*a*c)
    return (- b - d**0.5)/(2*a)

def Quadratic2():
    e = (b**2) - (4*a*c)
    return (- b - e**0.5)/(2*a)
while True:
    try:
        a = input("Give me a value of a ")
        b = input("Give me a value of b ")
        c = input("Give me a value of c ")
        if Quadratic() > 0 and Quadratic2() > 0:
            print("Thank you", Quadratic(), Quadratic2())
            break
    except:
        print("I don't understand please try again. ")