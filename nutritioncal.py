#Question 3  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
#
#~~~~~~~~~~~~~~~~~~~~~
# determine approx number of calories per hundred grams of a food product 
#requires 4 inputs; serving size (grams), grams of fat per serve, grams of carbs, grams of protein. Also needs the product name for output purposes 
# needs to calculate calories per 100g 

#input values of fat, carbs and protein per serve 

#need to use some form of tuple indexing here with list.index or something 
mylist = [60,10,10,10, "Nutella"), (60,10,10,10, "Oreos"), (60,10,10,10, "Muesli")]

#define constants
Fats = 9
Carbohydrates = 4
Proteins = 4


for r in mylist: 


    myfat = mylist[r](2)/mylist[r](1)
    mycarbs = mylist[r](3)/mylist[r](1)
    mypro = mylist[r](4)/mylist[r](1)
    prod = str(mylist[r](5))
    calories = (Fats*myfat + Carbohydrates*mycarbs + Proteins*mypro)*100
    print(f"{prod}: {calories}") 


