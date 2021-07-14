# Reads input numbers and return the total sum of the numbers, quantity of numbers and the average  
sum = total = 0
while True:
    num = input('Enter a number: ')
    if(num == 'done'):
        break
    try: 
        num = float(num)
    except: 
        print('Invalid input')
        continue 
    sum += num
    total += 1

print(f'Total Sum: {sum} \nTotal valid inputs: {total} \nAverage: {sum/total}')
