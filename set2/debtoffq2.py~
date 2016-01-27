def debt_year(balance, annualInterestRate, month_pay):
    debt = balance
    monthInterest = annualInterestRate/12.0
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    for iter in month:
        unpaid = debt - month_pay
        debt = unpaid + monthInterest*unpaid
        #end
    return debt


balance = 999999
annualInterestRate = 0.18

low = 0.0
high = balance/2.0
guess = (low+high)/2.0
debt = debt_year(balance, annualInterestRate, guess)
while abs(debt) > 0.001:
    debt = debt_year(balance, annualInterestRate, guess)
    if debt>0:
        low = guess
    elif debt<0:
        high = guess
    else:
        break
    guess = (high+low)/2.0
    #end
print('Lowest Payment Rate: ' + str(round(guess,2)))
