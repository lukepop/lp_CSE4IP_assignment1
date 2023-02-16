#Question 2  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
#
#~~~~~~~~~~~~~~~~~~~~~
# determine diabetes risk given user inputs of height (m), weight (kg) and the average number of hours spent exercising per week 
# based on inputs, calculate the BMI and then check health condition based on a complex boolean 
# 

#take input from user and store it as a float (it will default to str)
height = float(input('Height (m): '))
weight = float(input('Weight (kg): ')) 
activity = float(input('Average weekly activity (hours): ')) 

#calculate bmi, print(bmi) used for debugging purposes only and is commmented out in final code 
bmi = weight/(height**2)
#print(bmi)

#execute single complex boolean check of both conditions, else normal diabetes risk is present 
if (bmi > 25 and activity <3) or (bmi>30):
    print("High diabetes risk")
else:
    print("Normal diabetes risk")

