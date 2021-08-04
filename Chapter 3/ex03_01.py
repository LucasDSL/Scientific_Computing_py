
try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')
    quit()

if hours > 40:
    total = (hours - 40) * 1.5 * rate + 40 * rate
else: 
    total = hours * rate

print(f'Pay: {total}')