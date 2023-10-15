from sms import *
from roles import get_role_by_player_name
import time
import random

# COMMANDS
# hello: start listening to add players
# add foo: add player called foo
# start game: done assigning players
# assign: get new roles
# end game: set state to inactive

players = {}
state = 'inactive'  # one of ['inactive', 'add_players', 'active']
clear_all_messages()

while True:
    new_messages = get_new_messages()
    if new_messages:
        for latest_message in new_messages:
            content = latest_message.body.lower().strip()
            sender = latest_message.from_
            print(f'{sender} - {content}')
            if content.startswith("view "):
                _, name = content.split(" ", 1)
                role_to_send = get_role_by_player_name(name, roles)
                if role_to_send == 'hitler':
                    role_to_send = 'fascist'
                send_sms(sender, f"{name}'s party is {role_to_send}")
                random_player = random.choice(list(players.keys()))
                send_sms(players[random_player], f"{name}'s role was viewed.")

            if content == 'end game':
                players = {}
                clear_all_messages()
                state = 'inactive'
                send_sms(sender, "Game ended.")

            if state == 'inactive':
                if content == 'hello':
                    state = 'add_players'
                    send_sms(sender, "Game started. Add players.")

            if state == 'add_players':
                if content.startswith("add "):
                    _, name = content.split(" ", 1)
                    players[name] = sender
                    send_sms(sender, f"Added {name}. Text 'start game' to finish adding.")

                if content == 'start game':
                    player_count = len(list(players.keys()))
                    if player_count in [2,5,6,7,8,9,10]:
                        send_sms(sender, "Game ready. Text 'assign' to get roles.")
                        state = 'active'
                    else:
                        send_sms(sender, "Need 6-10 players to start the game.")

            if state == 'active':
                if content == 'assign':
                    roles = assign_and_notify_roles(players=players)
            print(players)
            print(state)    
    time.sleep(2)
