print("Mass to force calculator (kg -> N)\n")

correct_data_type = False

while correct_data_type == False:
    try: # This try-except block is used to stop the program if any non-numerical values are inputted for the variables startpoint, endpoint, step and g
        startpoint = float(input("Startpoint: "))
        endpoint = float(input("Endpoint: "))
        step = float(input("Step: ")) # How much the user wants to increase the value by each iteration
        g = float(input("Value of g: ")) # g is usually 9.81, but g is made an input in case the user wanted to input a value other than 9.81.
    
        if step <= 0:
            raise Exception("You cannot have a step that is equal to or smaller than 0. Please enter your step value again.")
    
    except ValueError:
        print("The values which you have entered are not numbers. Please enter the values again.") # This line will be executed if any non-numerical values are inputted
    else:
        correct_data_type = True

endpoint += step
count = startpoint
i = 0
print("\n") # Prints a new line

while i <= (endpoint // step): # This loop will stop when i is more than the value of endpoint DIV step
    ans = count * g
    print(f"{count:g} * {g:g} = {ans:g}") # The :g is there to remove any trailing zeros so that the result is easier to read
    count += step
    i += 1 # IMPORTANT! This line stops the program from running endlessly
