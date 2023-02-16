#Question 1  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
#
#~~~~~~~~~~~~~~~~~~~~~
# determine weight of an object in another planet given object weight (as user input) and other planets gravity (as user input)
# perform calculation of weight based on relative gravities and outputs weight on planet x as a string 

#take input from user and store it as a float (it will default to str)
weight = float(input('Your weight on Earth (kg): '))
planetgrav = float(input('Other planets gravity (m/s^2): '))

#earthgrav is a constrant 
EARTH_GRAVITY = 9.81

#calculate weight out and output this as a string using the f string notation 
weightout = weight/EARTH_GRAVITY*planetgrav
print(f"On the other planet, you would weigh: {weightout} kg",)

