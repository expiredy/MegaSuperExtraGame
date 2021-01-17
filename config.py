import random

def save(value):
    with open(path, 'wb') as f:
        f.write(bytes(str(value)), decode='UTF-8')
    return value

#_______________________________________dict's variables of keys_________________________________
connection_key = 'clientConnection'
address_key = 'ip'
name_key = 'name'
avatar_key = 'FacePictureThing'
disconect_message = 'He disconncted'

choicing_key = 'choicePlayer'

listener_key = 'listen'
sender_key = 'send'
room_key = ''
mafia_key = 'mafia'
doctor_key = 'doctor'
detective_key = 'detective'
inhabitants_key = 'inhabitants'
viewer_key = 'viewer'

#___________________________________________flags_for_game____________________________________

voiting = False
mini_games = False
sleeping = False
show_result = False

#____________________________________________game constans_____________________________________

classic_mode = 'classic'
configurate_mode = 'send_box'
game_mode = classic_mode
user_avatar = 'Sprites\Boi.jpg'
voiting_started = False
classic_order = {0: mafia_key, 1: doctor_key, 2: detective_key}

#____________________________________________nicknames___________________________________________
ExtraTHICCnames = ['ExtraAss228', 'Tom', 'Rapper № 1', 'Letov(Is he is fake one?)', 'CumCopter1488',
                   'CumBoi', 'Bo$$ of the Jimm', 'Cum',]


player_name = random.choice(ExtraTHICCnames)

#__________________________________________players roles___________________________________________
viewer = 'EyeInTheSky'
connected_user = 'user'
host_user = 'admin'


#_________________________________________players conditions_____________________________________
unplayable_condition = 'dead'
normal_condition = 'stay_awake'
condition_for_sleep = 'sleep'


#_________________________________________server's events_________________________________________
connected_event = 'connected'
start_event = 'start'
dead_event = 'dead'
message_sended = 'message_send'
vote_event = {mafia_key}


#___________________________________________servers data__________________________________________
path = 'data/server_config.txt'
main_room_id = 798532664717606922
server_id = 798338351086043136
server_token = ''
with open(path, 'rt') as f:
    read_data = f.read().split('\n')
    print(type(read_data))
    server = eval(read_data[0])
    room_id = eval(read_data[1])