class Category:

    # Instance variable called `ledger` that is a list.

    def __init__(self, name):
        self.name = name
        self.ledger = []


    # Format the text to the way it is supposed to be printed

    def __repr__(self):
        printing = f"{self.name:*^30}\n"
        total = 0.0

        for item in self.ledger:
            printing += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"

            total += item["amount"]

        printing += f"Total: {total:.2f}"

        return printing


    # A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`.

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})


    # A `withdraw` method that is similar to the `deposit` method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return `True` if the withdrawal took place, and `False` otherwise.

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})

            return True

        else:
            return False

    # A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.

    def get_balance(self):

        amounts_sum = 0.0
        for item in self.ledger:
            amounts_sum += item["amount"]

        return amounts_sum


    # A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return `True` if the transfer took place, and `False` otherwise.

    def transfer(self, amount, other):
        self.amount = amount
        self.other = other

        # Execute tranference and withdrawal of the specified amount

        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + other.name)
            other.deposit(amount, "Transfer from " + self.name)
            return True

        else:
            return False


    # A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method should be used by both the `withdraw` method and `transfer` method.

    def check_funds(self, amount):
        amounts_sum = 0.0

        for item in self.ledger:
            amounts_sum += item["amount"]

        if amount > amounts_sum:
            return False

        else:
            return True

    def total_withdrawals(self):
        total = 0.0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total



business = Category("Business")
food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# print(food)
# print(business)
# print(entertainment)
# test's parameters categories = [business, food, entertainment]



def create_spend_chart(categories):

    length = len(categories)

    # Total withdrawal of each object

    withdrawals_total_dict = {}
    for object in categories:
        withdrawals_total_dict[object.name] = abs(object.total_withdrawals())

    # Total withdrawals

    values = withdrawals_total_dict.values()
    withdrawal_total = sum(values)

    # Percentage spent of each category

    percentage_spent = {}
    for object in categories:
        percentage_spent[object.name] = withdrawals_total_dict[object.name] / withdrawal_total

    # List with the keys of the dictionary

    keys = percentage_spent.keys()

    #Length of the longer word

    max_length = 0
    for word in keys:
        if len(word) > max_length:
            max_length = len(word)


    chart = f"Percentage spent by category\n"

    for n in range(100, -1, -10):
        chart += f"{n:>3}| "
        for object in percentage_spent:
            if percentage_spent[object]*100 >= n:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + (3*length+1)*'-' +"\n"

    i = 0
    while max_length > i:
        chart += "     "
        for word in keys:
            if i < len(word):
                chart +=  f"{word[i]}  "
            else:
                chart += f"   "
        chart += "\n"
        i += 1

    chart = chart[:-1]

    print(chart)
    return chart

create_spend_chart([business, food, entertainment])
