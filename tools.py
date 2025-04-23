class Tool:
    def __init__(self, item_number, name, price, profit):
        self.item_number = item_number
        self.name = name
        self.price = price
        self.profit = profit

    def use(self):
        print(f'You used your { self.name } and earned ${ self.profit }!')

    def buy(self, money):
        print(f'You purchased { self.name }, you now have ${ money }')

    def __repr__(self):
        return f'{ self.item_number } { self.name } (Price: ${ self.price }, Profit: ${ self.profit })'




tools = [
    Tool('1.', 'Teeth', 0, 1),
    Tool('2.', 'Rusty Scissors', 5, 5),
    Tool('3.', 'Push Lawnmower', 25, 50),
    Tool('4.', 'Battery-Powered Lawnmower', 250, 100),
    Tool('5.', 'Team', 500, 250)
]