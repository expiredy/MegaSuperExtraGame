import random
import config
connected_players = {}

class Player:
    def __init__(self, id, name=random.choice(condig.ExtraTHICCnames), role=None, avatar=None,
                 condition=config.normal_condition):
        self.id, self.name, self.role, self.condition = id, name, role, condition
        self.avatar = avatar

    def set_role(self, new_role):
        self.role = new_role

    def is_alive(self):
        return condition != config.unplayable_condition

    def make_viewer(self):
        self.condition = config.unplayable_condition

    def awake(self):
        self.condition = config.condition_for_sleep


def temporary_measure_to_create_player():
    player_name = input('Введите имя игрока')
    player_image = input()
    player_role = None

temporary_measure_to_create_palaer()
mode = config.classic_mode
amount_players =  int(input("Сколько игроков в игре? "))
amount_mafia = int(input("Сколько мафий в игре? "))
amount_doctors = 1
amount_detectives = 1
players = {}

if mode == config.configurate_mode:
    amount_doctors = int(input("Сколько докторов в игре? "))
    amount_detectives = int(input("Сколько детективов в игре? "))
total_players = list(range(0, amount_players))
random.shuffle(total_players)
players[config.mafia_key] = [total_players.pop() for _ in range(amount_mafia)]
players[config.doctor_key] = [total_players.pop() for _ in range(amount_doctors)]
players[config.detective_key] = [total_players.pop() for _ in range(amount_detectives)]
if mode != config.classic_mode:
    pass
players[config.inhabitants_key] = total_players

for key in list(config.classic_order.keys()):
    for _ in range(len(players[config.classic_order[key]])):
        print(player, 'is', config.classic_order[key])
print(', '.join(players[config.inhabitants_key]), "is", config.inhabitants_key)


while all([mafia.is_alive() for mafia in players[config.mafia_key]):
    pass