from player import Player
from tools import tools, Tool




money = 0
player_tools = [tools[0]]
days_worked = 0
has_team = False


def start_game():
    print('Welcome to Landscaper!')
    
    name = input('What is your name? ').capitalize()
    print(f'\nHello, { name }! Let\'s get started!')
    
    handle_user_selection()
    
    
    
    # Player(name, 0, ['Teeth'], 0, False)
    # print(f'{ name }, you have ${ money }, and have worked { days_worked } days, and your current tools are { tools }.')


def handle_user_selection():
    print('\nWhat would you like to do? (enter \'1\' or \'2\')')
    
    player_selection = input('1. Cut grass    2. Visit the store ')
    if player_selection == '1':
        mow_lawn()
    elif player_selection == '2':
        print('store')
    else:
        print('Please enter a valid selection (1 or 2)')
        handle_user_selection()


def mow_lawn():
    tools[0].use()
    global money 
    money += tools[0].profit
    print(f'\nyou have ${ money }.')
    handle_user_selection()



start_game()

