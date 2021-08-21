import budget as b 

business = b.Category("Business")
entertainment  = b.Category("Entertainment")
food = b.Category("Food")

def test_str():
    '''
    print(business)
    print(entertainment)
    print(food)
    '''

def test_deposit():
    business.deposit(1000, "money")
    print(business.get_balance())

# test_str_and_create_class()
'''test_deposit()
print(business.withdraw(1001, "taking everything"))
print(business.withdraw(999, "almost everything"))
print(business.check_funds(1))
print(business.check_funds(10))'''

# testing Category.transfer()
'''business.deposit(100, "money100")
food.deposit(100, "Money100")
print(business.transfer(20, food))
print(business.ledger)
print(food.ledger)'''

'''business.deposit(100, "money100")
food.deposit(100, "Money100")
food.transfer(40, entertainment)
business.transfer(20, food)

print(business)'''