#Question 3  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230216
# B - 20230217 Update code structure to use dictionaries
# C - 20230302 Update based on comments from forums. Also need food name as an input. 
#              The order of the nutrients is in an order so a list is appropriate for values
#              The mixed data data type makes a dictionary appropriate. Checked   
#              
#~~~~~~~~~~~~~~~~~~~~~
# TODO:  N/A
#
# determine approx number of calories per hundred grams of a food product 
#requires 4 inputs; serving size (grams), grams of fat per serve, grams of carbs, grams of protein. Also needs the product name for output purposes 
# needs to calculate calories per 100g 

#input values of fat, carbs and protein per serve, serving size

#define constants
FATS = 9 
CARBS = 4
PROTEIN = 4 

#as per the forum takes in all arguments in a single run. Nutrition [serv_size,fat,carbs,protein]
my_foods = {"Nutella": [15, 4.6, 8.6, 0.9], "Oreos": [34, 7, 25, 1], "Muesli": [50, 6, 32, 6]} 
            
for keys in my_foods:
    # keys will preserve the name of the food, food is the list of nutrients in the order given by 
    # the assignment prompt 
    
    #print(keys)
    food = my_foods[keys] 
    #print(food)
    
    #question prompt specifies order of serving size, fat, carbohydrates, protein per serve. This order is used in the input list of dictionaries 
    #and is relief on for the array order for the 
    serving_size = food[0]
    # calculate the quantity of each nutrient in grams by first dividing the nutrient in a serve
    # by the serving size and then multiplying by 100 to calculate nutrient_100g. Needs to be a float 
    fat_100g = float((food[1]/serving_size)*100)
    carbs_100g = float((food[2]/serving_size)*100)
    protein_100g = float((food[3]/serving_size)*100)
    
    #print(fat_100g,carb_100g,pro_100g)
    
    #this is where the calories per 100g is calculated by multiplying each nutrient_100g by the calorie
    #constant for each nutrient type 
    
    calories_100g = (fat_100g)*FATS + (carbs_100g)*CARBS + (protein_100g)*PROTEIN 
    print(f'{keys}: {calories_100g}')
  
        
        
        
        
