balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

month = [1,2,3,4,5,6,7,8,9,10,11,12]
rem_bal = balance
mon_inter = annualInterestRate/12.0
mon_pay = monthlyPaymentRate
total_pay = 0

for iter in month:
    min_pay = rem_bal*mon_pay
    total_pay+= min_pay
    mon_unpaid = rem_bal - min_pay
    rem_bal = mon_unpaid + mon_inter*mon_unpaid
    print('Month: ' +str(iter))
    
    print('Minimum monthly payment: '+ str(round(min_pay,2)))

    print('Remaining balance: '+ str(round(rem_bal,2)))
    #Fim do for

print('Total paid: ' + str(round(total_pay,2)))
print('Remaining balance: ' +str(round(rem_bal,2)))



          
