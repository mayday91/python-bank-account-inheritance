class BankAccount:
  def __init__(self, balance):
    self.balance = balance

  def __str__(self):
    return 'This account has ${}'.format(self.balance)

  def deposit(self, amount):
    print(f'cha-ching! your account just had ${amount} added!')
    self.balance += amount

  def withdraw(self, amount):
    print('Take my money')
    self.balance -= amount

  def accumulate_interest(self, amount=0.02):
    self.balance = self.balance + (self.balance * amount)
    return self.balance

class ChildrensAccount:
  def __init__(self, balance):
    self.balance = balance

  def __str__(self):
    return 'This account has ${}'.format(self.balance)

  def deposit(self, amount):
    print(f'cha-ching! your account just had ${amount} added!')
    self.balance += amount

  def withdraw(self, amount):
    print('Take my money')
    self.balance -= amount

  def accumulate_interest(self, amount=10):
    self.balance = self.balance + amount
    return self.balance

class OverdraftAccount:
  def __init__(self, balance):
    self.balance = balance
    self.overdraft_penalty = 40

  def __str__(self):
    return 'This account has ${}'.format(self.balance)

  def deposit(self, amount):
    print(f'cha-ching! your account just had ${amount} added!')
    self.balance += amount

  def withdraw(self, amount):
    print('Take my money')
    self.balance -= amount
    if self.balance < 0:
      self.balance -= self.overdraft_penalty
      print('oh no! overdraft fees just hit for ${self.overdraft_penalty}')
      print(f'you now have ${self.balance} in your account.')

  def accumulate_interest(self, amount=0.02):
    self.balance = self.balance + (self.balance * amount)
    return self.balance

basic_account = BankAccount(100)
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount(100)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount(1400)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))
