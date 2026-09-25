num = 0
counter = 0
while counter < 10:
    user_inpt = int(input(f'Please enter your {counter + 1} digit out of 10: '))
    if user_inpt%2 != 0 and user_inpt > num:
        num = user_inpt
    counter += 1

if num == 0:
    print(f"No Odd Number was added")
else:
    print(f"The Highest Odd Number entered was {num}")
    
