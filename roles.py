from random import shuffle

def generate_roles(num_players):
    roles_map = {
        2: ['liberal', 'fascist'],
        5: ['liberal']*3 + ['fascist'] + ['hitler'],
        6: ['liberal']*4 + ['fascist'] + ['hitler'],
        7: ['liberal']*4 + ['fascist']*2 + ['hitler'],
        8: ['liberal']*5 + ['fascist']*2 + ['hitler'],
        9: ['liberal']*5 + ['fascist']*3 + ['hitler'],
        10: ['liberal']*6 + ['fascist']*3 + ['hitler']
    }
    
    roles = roles_map[num_players]
    shuffle(roles)

    return roles

def get_role_by_player_name(target_player, zipped_data):
    for player, role in zipped_data:
        if player == target_player:
            return role
    return "Player not found"