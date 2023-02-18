#Question 3  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230217
# 
#~~~~~~~~~~~~~~~~~~~~~
# take user input of integers only, including 0 and only support whole numbers years (integers) 
# 
#  input initial deposit amount 
deposit = float(input("Deposit amount ($): "))

#  input initial deposit amount 
interest = float(input("Interest rate (%): "))

# check on years, if a non integer is parsed then the code loops until the while condition i !=0 is met 
i = 0 
while i == 0: 
    try:
        years = int(input("Years invested:")) 
        i = 1
    except: 
        i = 0 

#create a list to loop through for n number of years 
n = 0 
while n <= years: 
    if n == 0: 
        balance = deposit 
        n+=1
    else: 
       balance = balance+balance*(interest/100)
       n+=1   
print(f"Balance after {years} years: ${balance}")