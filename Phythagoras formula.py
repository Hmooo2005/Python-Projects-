# function to calculate the length of the ____(Phythagoras formula)
#--------------------------------------------
def water(n1 ,n2):                        
    try:                                   
        import math                       
        n3 = (n1**2)+(n2**2)              
        return math.sqrt(n3)              
    except ValueError:                    
        print("please enter a number!!") 

print(water(145, 133.3))                                     
#---------------------------------------------



