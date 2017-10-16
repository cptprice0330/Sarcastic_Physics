import math


def twoNumberInsideInputValidate(I1, I2, testSubject):  # Checks if a value is within a set range
    valid = False
    while not valid:
        if testSubject < I1:
            testSubject = float(input("Input too low: "))
        if testSubject > I2:
            testSubject = float(input("Input too high: "))
        else:
            valid = True


def twoNumberOutsideInputValidate(I1, I2, testSubject):  # Checks if a value is outside a set range
    valid = False
    while not valid:
        if testSubject > I1:
            testSubject = float(input("Input above range: "))
        if testSubject < I2:
            testSubject = float(input("Input Below range: "))
        else:
            valid = True


def timeConverter(time):  # Time is 5 part list
    for i in range(0, 5):
        if time[i] != 0:
            if i == 0:
                time[1] = time[0] / 60
                time[2] = time[1] / 60
                time[3] = time[2] / 24
                time[4] = time[3] / 365.25
            if i == 1:
                time[0] = time[1] * 60
                time[2] = time[1] / 60
                time[3] = time[2] / 24
                time[4] = time[3] / 365.25
            if i == 2:
                time[1] = time[2] * 60
                time[0] = time[1] * 60
                time[3] = time[2] / 24
                time[4] = time[3] / 365.25
            if i == 3:
                time[2] = time[3] * 24
                time[1] = time[2] * 60
                time[0] = time[1] * 60
                time[4] = time[3] / 365.25
            if i == 4:
                time[3] = time[4] * 365.25
                time[2] = time[3] * 24
                time[1] = time[2] * 60
                time[0] = time[1] * 60


def Factorial(x):
    fac = 1
    for i in range(2, x + 1):
        fac *= i
    return fac

def Binomial(n,k):
    if k !=n:
       bCoeff = (Factorial(n))//((Factorial(k)*(Factorial(n-k))))
    else:
        bCoeff = 1
    return bCoeff
