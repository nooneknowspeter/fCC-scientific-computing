class Category:
    def __init__(self, category: str):
        self.category = category
        self.ledger: list[dict] = []

    def __str__(self):
        object_information: str = ""
        title: str = self.category.center(30, "*")
        object_information += f"{title}\n"

        for dict in self.ledger:
            try:
                description: str = dict["description"][0:23]
            except:
                description: str = ""

            amount: str = f"{dict['amount']:.2f}"
            object_information += f"{description:<23}{amount:>7}\n"

        withdrawal_total: str = f"Total: {self.get_balance()}"
        object_information += withdrawal_total

        return object_information

    def deposit(self, amount: float, description: str = ""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum([dict["amount"] for dict in self.ledger])

    def transfer(self, amount: float, object) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount=amount, description=f"Transfer to {object.category}")
            object.deposit(amount=amount, description=f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount: float) -> bool:
        return amount <= self.get_balance()


def create_spend_chart(categories):
    # dictionary to store withdrawal total for each category
    withdrawal_amounts = {}

    # iterate through ledger of each category object, sum up their withdrawals
    # (negative numbers) and store them in key value pairs
    for category in categories:
        category_withdrawal_total = 0
        for ledger in category.ledger:
            if ledger["amount"] < 0:
                category_withdrawal_total += abs(ledger["amount"])
        withdrawal_amounts[category.category] = round(category_withdrawal_total, 2)

    # find total amount of all withdrawals from each category
    withdrawal_total = sum(withdrawal_amounts.values())
    # dictionary to store percentages for each category
    percentages = {}

    # iterate through withdrawal amount dictionary
    for category in withdrawal_amounts.keys():
        # ( amount // total ) * 100
        percentages[category] = int(
            round(withdrawal_amounts[category] / withdrawal_total, 2) * 100
        )

    chart = ""
    title = "Percentage spent by category\n"
    chart += title

    for i in range(100, -10, -10):
        chart += f"{i}".rjust(3) + "| "
        for percent in percentages.values():
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += " " * 4 + "-" * (len(percentages.values()) * 3 + 1)
    chart += "\n     "
    dict_key_list = list(percentages.keys())
    max_len_category = max([len(i) for i in dict_key_list])

    for i in range(max_len_category):
        for category in dict_key_list:
            if len(category) > i:
                chart += category[i] + "  "
            else:
                chart += "   "
        if i < max_len_category - 1:
            chart += "\n     "

    return chart


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    clothing.deposit(1000, "deposit")
    clothing.withdraw(45.15, "shirt")
    clothing.withdraw(80.89, "pants")
    print(create_spend_chart([food, clothing]))
