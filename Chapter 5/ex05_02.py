# Shows the maximum and minimum values from a list of numbers 
max = min = None
while True:
    num = input('Enter a number: ')
    if(num == 'done'):
        break
    try: 
        num = float(num)
    except: 
        print('Invalid input')
        continue 
    if max is None and min is None:
        max = num
        min = num 
    elif num > max:
        max = num 
    else: 
        min = num 
print(f'Largest numeric input: {max}\nSmallest numeric input: {min}')
