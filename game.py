from player import Player
from tools import tools, Tool
import os, sys



def clear():
    os.system('clear || cls')




def start_game():
    global player
    
    clear()
    print('Welcome to Landscaper!')
    
    name = input('What is your name? ').capitalize()
    player = Player(name)
    player.tools.append(tools[0])
    player.current_tool = tools[0]
    
    clear()
    print(f'Hello, { name }! Let\'s get started!')
    
    handle_user_selection()




def handle_user_selection():
    print('\nWhat would you like to do? (enter \'1\' or \'2\')')
    
    selection = input('1. Cut grass     2. Visit the store      3. Quit Game\n').strip()
    if selection == '1':
        mow_lawn()
    elif selection == '2':
        visit_store()
    elif selection == '3':
        print('Exiting Game.')
        sys.exit(0)
    else:
        clear()
        print('Please enter a valid selection (1 or 2)')
        handle_user_selection()




def mow_lawn():
    clear()
    player.use_tool()
    print(f'\nYou now have ${ player.money }.')
    handle_user_selection()




def visit_store():
    clear()
    print(f'You have ${ player.money }. What would you like to purchase?\n')

    for tool in tools:
        print(f'{ tool.item_number } { tool.name } - ${ tool.price } | Profit: ${ tool.profit }')

    selection = input('\nEnter the number of the tool you\'d like to buy: ').strip()

    if selection == '1':
        selected_tool = tools[0]
    elif selection == '2':
        selected_tool = tools[1]
    elif selection == '3':
        selected_tool = tools[2]
    elif selection == '4':
        selected_tool = tools[3]
    elif selection == '5':
        selected_tool = tools[4]
    else:
        print('Invalid selection.')
        visit_store()

    if selected_tool in player.tools:
        visit_store()
        print(f'You already own { selected_tool.name }.')
        
    elif player.money >= selected_tool.price:
        player.money -= selected_tool.price
        player.tools.append(selected_tool)
        player.current_tool = selected_tool
        clear()
        print(f'You bought { selected_tool.name }. It\'s now your active tool.')
    else:
        print(f'Not enough money to buy {selected_tool.name}.')


    handle_user_selection()



start_game()