try:
    numerator= int(input("enter a number to device: "))
    deominator= int(input("enter a number to devide by: "))
    result= numerator/deominator
   
except ZeroDivisionError as e:
    print(e)
    print("you can't devided by zero! idiot! ")
    
except ValueError as e:
    print(e)
    print("enter only number plz")    
        
except Exception as e:
    print(e)
    print("something went wrong :(")   
    
else:
    print(result) 

finally:
    print("This wall always exucute")             