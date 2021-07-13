def computeGrade(grade): 
    try : 
        grade = float(grade)
    except:
        print('Error - please enter numeric value.')
        quit()
    
    if grade > 1.0 or grade < 0: 
        print('Error - please enter a numeric value between 0 and 1 (inclusive).')
        quit()

    if grade >= 0.9:
        print('A')
    elif grade >= 0.8:
        print('B')
    elif grade >= 0.7:
        print('C')
    elif grade >= 0.6:
        print('D')
    else:
        print('F')

grade = input('Enter grade: ')
computeGrade(grade)
