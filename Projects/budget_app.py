class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = list()
  
  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount,
    "description": description})
  
  def withdraw(self, amount, description=''):
    total_money = None
    for obj in self.ledger: 
      if total_money == None: 
        total_money = 0
      total_money += obj.amount
      if total_money <= 0: 
        return False
    self.ledger.append({"amount": amount*(-1), 
    "description": description})
    return True
  def get_balance(self):
    print('')

def create_spend_chart(categories):
  print('')