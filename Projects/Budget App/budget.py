class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = list()

  def deposit(self, amount, description=''):
    self.ledger.append({"amount": amount,
    "description": description})
  
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({"amount": amount*(-1), 
      "description": description})
      return True
    return False

  def get_balance(self):
    balance = 0
    for obj in self.ledger: 
      balance += obj["amount"]
    return balance

  def transfer(self, amount, budget_category_destination): # Implement check_funds
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category_destination.category}")
      Category.deposit(budget_category_destination, amount, f"Transfer from {self.category}")
      return True
    return False 

  def check_funds(self, amount):
    total_balance = self.get_balance()
    if amount > total_balance:
      return False 
    return True

  def __str__(self) -> str:
      return "*{^}           *".format(self.category)


def create_spend_chart(categories):
  print('')
