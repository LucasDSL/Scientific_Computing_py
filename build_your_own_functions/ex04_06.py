hours = input('Enter the hours: ')
rate = input('Enter the rate: ')
def calculatePay(hours, rate):
    try: 
        hoursWithinTheFunction = int(hours)
        rateWithinTheFunction = float(rate)
    except: 
        print('Error, please enter numeric input')
        quit()

    if (hoursWithinTheFunction > 40):
        pay = (hoursWithinTheFunction - 40) * rateWithinTheFunction * 1.5 + 40 * rateWithinTheFunction
    
    print(f'Pay: {pay}')

calculatePay(hours, rate)