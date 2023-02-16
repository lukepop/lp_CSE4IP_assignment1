#Question 1  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
#
#~~~~~~~~~~~~~~~~~~~~~
# determine weight of an object in another planet given object weight (ass user input)
#function only uses the planet name and returns a string indicating the planets gravity and the objects weight on the other planet

#take input from user and store it as a float (it will default to str)
weight = float(input('Your weight on Earth (kg): '))
planetgrav = float(input('Other planets gravity (m/s^2): '))

#earthgrav is a constrant 
earthgrav = 9.81

#calculate weight out and output this as a string using the f string notation 
weightout = weight/earthgrav*planetgrav
print(f"On the other planet, you would weigh: {weightout} kg",)

