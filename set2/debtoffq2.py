def debt_year(balance, annualInterestRate, month_pay):
    debt = balance
    monthInterest = annualInterestRate/12.0
    month = [1,2,3,4,5,6,7,8,9,10,11,12]
    for iter in month:
        unpaid = debt - month_pay
        debt = unpaid + monthInterest*unpaid
        #end
    return debt


balance = 3329
annualInterestRate = 0.2

guess = 10
debt = debt_year(balance, annualInterestRate, guess)
while debt > 0.001:
    guess +=10
    debt = debt_year(balance, annualInterestRate, guess)
    #print(str(guess))
    #end
    
print('Lowest Payment Rate: ' + str(int(guess)))
