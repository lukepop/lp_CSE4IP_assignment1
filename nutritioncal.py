#Question 3  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
# B - 20230217 Update code structure to use dictionaries 
#~~~~~~~~~~~~~~~~~~~~~
# determine approx number of calories per hundred grams of a food product 
#requires 4 inputs; serving size (grams), grams of fat per serve, grams of carbs, grams of protein. Also needs the product name for output purposes 
# needs to calculate calories per 100g 

#input values of fat, carbs and protein per serve 

#need to use some form of tuple indexing here with list.index or something 
#mylist = [60,10,10,10, "Nutella"), (60,10,10,10, "Oreos"), (60,10,10,10, "Muesli")]

#define constants
FATS = 9 
CARBS = 4
PROTEIN = 4 

my_foods = {"Nutella": [{"serving_size":60}, {"Fats":10}, {"Carbohydrates":20}, {"Protein":20}], "Oreos": [{"serving_size":20}, {"Fats":10}, {"Carbohydrates":5}, {"Protein" :5}]}
for keys in my_foods:
    # keys will preserve the name of the food, food is the list of the dictionaries relating to that food
    food = my_foods[keys]
    
    #question prompt specifies order of serving size, fat, carbohydrates, protein per serve. This order is used in the input list of dictionaries 
    #and is relief on for the array order for the 
    serve = food[0].get("serving_size")
    # calculate the serving size in grams 
    fat_100g = (food[1].get("Fats")/serve)*100
    carb_100g = (food[2].get("Carbohydrates")/serve)*100
    pro_100g = (food[3].get("Protein")/serve)*100
    
    calories = (fat_100g)*FATS + (carb_100g)*CARBS + (pro_100g)*PROTEIN 
    print(f'{keys}: {calories}')
    

  
        
        
        
        
