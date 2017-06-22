#Grader:
import math
'''
def polysum(n,s):
    area = 0.25*n*s**2/math.tan(math.pi/n)
    square = (s*n)**2
    return round(area+square,4)
'''

# Paying Debt off in a Year:

# Problem 1
def payingDebt(balance,annualInterestRate,monthlyPaymentRate):
    '''print out the balance after one year'''

    for month in range(1,13):
        if month==1:
            updateBalance = balance + balance * (annualInterestRate/12)
        else:
            updateBalance = perviousBalance + perviousBalance*(annualInterestRate/12)
        unpaidBalance = updateBalance - updateBalance * monthlyPaymentRate
        perviousBalance = unpaidBalance

        if month==12:
            return round(unpaidBalance,2)


#print('Remaining balance: ' +str(payingDebt(balance,annualInterestRate,monthlyPaymentRate)))

# Problem 2
def fixedPay(balance,annualInterestRate):

    def finalDebt(balance,annualInterestRate,fixed):
        for month in range(1,13):
            if month==1:
                updateBalance = balance + balance * (annualInterestRate/12)
                perviousBalance = balance
            else:
                updateBalance = unpaidBalance + (annualInterestRate/12)*unpaidBalance
                perviousBalance = updateBalance
            unpaidBalance = perviousBalance - fixed

            if month==12:
                return unpaidBalance

    fixed = 10
    while finalDebt(balance,annualInterestRate,fixed)>0:
        fixed+=10
    return fixed

# print ('Lowest Payment: '+str(fixedPay(balance,annualInterestRate)))

# Problem 3
'''Using Bisection Search to Make the Program Faster'''


def finalDebt(balance, annualInterestRate, fixed):
    for month in range(1, 13):
        if month == 1:
            updateBalance = balance + balance * (annualInterestRate / 12)
            perviousBalance = balance
        else:
            updateBalance = unpaidBalance + (annualInterestRate / 12) * unpaidBalance
            perviousBalance = updateBalance
        unpaidBalance = perviousBalance - fixed

        if month == 12:
            return unpaidBalance


def bisection(balance,annualInterestRate):
    lowerBound = balance/12
    upperBound = (balance*((1+annualInterestRate/12)**12))/12
    guess = (lowerBound+upperBound)/2
    final = finalDebt(balance,annualInterestRate,guess)

    while abs(final)>0.05: # Stop when Get in a small range
        if final>0:
            lowerBound=guess
        else:
            upperBound=guess
        guess = (lowerBound + upperBound) / 2
        final = finalDebt(balance, annualInterestRate, guess)


    return guess

#print (bisection(320000,0.2)) #29157.09
#print(bisection(999999,0.18)) #90325.03
#print('Lowest Payment: '+str(round(bisection(balance,annualInterestRate),2)))


