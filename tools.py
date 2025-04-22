class Tool:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

    def use(self):
        print(f"\nYou used your { self.name } and earned ${ self.profit }!")

    def __repr__(self):
        return f"{ self.name } (Price: ${ self.price }, Profit: ${ self.profit })"




tools = [
    Tool('Teeth', 0, 1),
    Tool('Rusty Scissors', 5, 5),
    Tool('Push Lawnmower', 25, 50),
    Tool('Battery-Powered Lawnmower', 250, 100),
    Tool('Team', 500, 250)
]