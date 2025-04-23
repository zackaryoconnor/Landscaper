class Player:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.tools = []
        current_tool = None
        # self.days_worked = days_worked
        # self.has_team = has_team

    
    def use_tool(self):
        if self.current_tool:
            self.current_tool.use()
            self.money += self.current_tool.profit
        else:
            print('You don\'t have any tools')