from twilio.rest import Client
import time
from roles import generate_roles

import os
from dotenv import load_dotenv
load_dotenv()

phone_number = os.environ.get("TWILIO_PHONE_NUM")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def get_new_messages():
    new_messages = []
    
    messages = client.messages.list(
        to=phone_number,
        limit=10
    )

    time.sleep(1)
    for message in reversed(messages):
        new_messages.append(message)
        message.delete()  # delete the message from Twilio after processing
    
    return new_messages

def assign_and_notify_roles(players):
    num_players = len(players.keys())

    roles = generate_roles(num_players)

    for name, role in zip(players.keys(), roles):
        # if liberal, or hitler when hitler doesn't know their team
        if role == 'liberal' or (num_players>6 and role == 'hitler'):
            send_sms(players[name], f"Your role is: {role}")

        # if liberal, or hitler when hitler knows their team
        if role == 'fascist' or (num_players<=6 and role == 'hitler'):
            message = f'Your role is: {role}. Fascists are: '
            for name2, role2 in zip(players.keys(), roles):
                if role2 != 'liberal' and name != name2:
                    message += f'({name2} is {role2})'
            send_sms(players[name], message)

    return zip(players.keys(), roles)

def send_sms(to, body):
    client.messages.create(
        body=body,
        from_=phone_number,
        to=to
    )

def clear_all_messages():
    messages = client.messages.list(
        to=phone_number,
        limit=50
    )
    for message in messages:
        message.delete()
