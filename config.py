import random

def save(value, number):
    with open(server_path, 'r+') as f:
        read_data = f.read()
        f.truncate()
        for data_line in read_data.split('\n')[:number]:
            f.write(str(data_line))
        f.write(str(value))
        for data_line in read_data.split('\n')[number + 1:]:
            f.write(str(data_line))
    return value

def give_info():
    return str({name_key: player_name})

#______________________________________________pathes__________________________________________
# name_path = 'data/username.txt'
# server_path = 'data/server_config.txt'
# launch_path = 'data/launch_config.txt'
# game_path = 'data/game_flags_config.txt'
#_______________________________________dict's variables of keys_________________________________
connection_key = 'clientConnection'
address_key = 'ip'
name_key = 'name'
avatar_key = 'FacePictureThing'
disconect_message = 'He disconncted'

choicing_key = 'choicePlayer'

context_key = 'context'
author_key = 'author'

listener_key = 'listen'
sender_key = 'send'
role_key = 'role'
room_key = ''
mafia_key = 'mafia'
doctor_key = 'doctor'
detective_key = 'detective'
inhabitants_key = 'inhabitants'
viewer_key = 'viewer'
#__________________________________________players roles___________________________________________
viewer = 'EyeInTheSky'
connected_user = 'user'
host_user = 'admin'


#___________________________________________flags_for_game____________________________________
voiting = False
mini_games = False
sleeping = False
show_result = False
player_choiced = False
accepting = False
#____________________________________________game constans_____________________________________

classic_mode = 'classic'
configurate_mode = 'send_box'
game_mode = classic_mode
user_avatar = 'Sprites\Boi.jpg'
voiting_started = False
classic_order = {0: mafia_key, 1: doctor_key, 2: detective_key}
amount_mafia = 1
amount_doctors = 1
amount_detectives = 1
role = host_user

#____________________________________________nicknames___________________________________________
ExtraTHICCnames = ['ExtraAss228', 'Tom', 'Rapper № 1', 'Letov(Is he is fake one?)', 'CumCopter1488',
                   'CumBoi', 'Bo$$ of the Jimm', 'Cum',]


player_name = random.choice(ExtraTHICCnames)


#_________________________________________players conditions_____________________________________
unplayable_condition = 'dead'
normal_condition = 'stay_awake'
condition_for_sleep = 'sleep'


#_________________________________________server's events_________________________________________
listen_players = True
connected_event = 'connected'
dead_event = 'dead'
got_mail_event = 'U_got_mail'
game_start_event = 'game_started'
message_sended = 'message_send'
change_info_event = 'change_info'
vote_event = {mafia_key}
game_over = 'game_is_over'

#___________________________________________servers data__________________________________________

server = None
players = {}
total_players_updated = False
chat_history = {}
# main_room_id = 798532664717606922
# server_id = 798338351086043136
# server_token = ''
# with open(server_path, 'r+') as f:
#     read_data = f.read().split('\n')
#     print(type(read_data))
#     server = eval(read_data[0])
#     room_id = eval(read_data[1])