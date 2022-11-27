def Quadratic():
    e = (b**2) - (4*a*c)
    return (- b + e**0.5)/(2*a)
while True:
    try:
        a = int(input("Give me a value of a "))
        b = int(input("Give me a value of b "))
        c = int(input("Give me a value of c "))
        if Quadratic() > 0:
            print("Thank you", Quadratic())
            break
    except:
        print("I don't understand please try again. ")