#Question 5  
# REV HISTORY
#~~~~~~~~~~~~~~~~~~~~~
# A - 20230228 LDP Tested and checked 
# 
#~~~~~~~~~~~~~~~~~~~~~
# TODO: Check LMS forum for outcome of queries 
# 
# 
# accept input and print smallest appropriate powerbank size 

# Part A 
#1 defining the constants
SMALL_MAH = 3000
MEDIUM_MAH = 10000
LARGE_MAH = 20000


#powerbank size is an array, no user input cell is output in the run code 
powerbank_size = [2000,9999,3000,12000]

#iterates over the rows in the array, the rows value will be the value of the row in that array 
for rows in powerbank_size: 
    if rows <= SMALL_MAH: #checks the condition against the small powercell, if this is True it loops again through the next row value 
        print('small')
    
    elif rows <= MEDIUM_MAH: # checks the condition against the medium powercell, if this True then it loops again through the next row value 
        print('medium')
    else: 
        print('large') #if it is not small or medium, it must be large. All sizes above large are also large so it makes sense this belongs to the else 
        
#Part B 

print('Enter information about the devies you wish to charge')



#initialise it as True with the test subsequent to check if more devices are required    
more_devices = True 
powerbank_total = 0 

while more_devices == True: 
    powerbank_input = float(input("Device battery capacity (mAh): "))
    #print(powerbank_total)
    
    test = str(input("More? (y/n): "))
    #print(test)
    if test == 'y': 
        more_devices = True
        powerbank_total += powerbank_input 
    elif test == 'n': 
        more_devices = False 
        powerbank_total += powerbank_input 
    else: 
        break 

print(f"Total required battery capacity: {int(powerbank_total)} mAh")

if powerbank_total <= SMALL_MAH: #checks the condition against the small powercell, if this is True it loops again through the next row value 
    powerbank_rec = 'small'
    
elif powerbank_total <= MEDIUM_MAH: # checks the condition against the medium powercell, if this True then it loops again through the next row value 
    powerbank_rec ='medium'
else: 
    powerbank_rec ='large' #if it is not small or medium, it must be large. All sizes above large are also large so it makes sense this belongs to the else 

print(f"Power bank recommendation: {powerbank_rec}")
