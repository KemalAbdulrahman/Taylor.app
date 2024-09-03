import math

#First approach
def approximation1(x, nth_term):
    result = 0
    for a in range(nth_term):
        calculation = ((x**a)/math.factorial(a))
        if(a == 0):
            result += 1
        elif(a == 1):
            result -= x
        elif(a%2 == 0):
            result += calculation
        elif(a%2 != 0):
            result -= calculation
        calculation = 0

    print(result)

#second approach
def approximation2(x, nth_term):
    result = 0
    calculation = 0
    for a in range(nth_term):
        calculation += ((x**a)/math.factorial(a))

    result = 1/calculation
    print(result)


#main program
print("True value of e^-5: ")
print("0.006737947")
print("Approximation 1 (n = 20): ")
approximation1(5, 20)
print("Approximation 2 (n = 20): ")
approximation2(5, 20)
print("Approximation 1 (n = 100): ")
approximation1(5, 100)
print("Approximation 2 (n = 100): ")
approximation2(5, 100)

