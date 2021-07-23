numbers = []
while True:
    number = input('Enter a number: ')
    if number == 'done': break
    try: 
        number = float(number)
    except: 
        print('Enter a numeric input')
        continue 
    numbers.append(number)
print(f'Max: {max(numbers)}')
print(f'Min: {min(numbers)}')