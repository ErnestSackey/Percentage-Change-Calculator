def percentage_change_calculator():
    while True:
        try:
            original_number = int(input('What is the original number:')) #take the original number from user
            break
        except:
            print("That's not a valid number!") #handling non numeric numbers
    while True:
        try:
            new_number = int(input('What is the new number:')) #take the new number from user
            break
        except:
            print("That's not a valid number!")
    difference = new_number - original_number #calculates the difference 
    if difference > 0:
        print(f'There is an increase of: {difference}')
    else:
        print(f'There is an decrease of: {difference}')
    percent_difference = round((difference / original_number) * 100, 2) #calculates the % difference
    if difference > 0:
        print(f'With a % increase of: {percent_difference}%')
    else:
        print(f'With a % decrease of: {percent_difference}%')
        
percentage_change_calculator()