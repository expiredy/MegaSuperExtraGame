import random
import config
total_players = {}

class Player:
    def __init__(self, id, name, role=None, condition=config.normal_condition):
        self.id, self.name, self.role, self.condition = id, name, role, condition

    def set_role(self, new_role):
        self.role = new_role

    def is_alive(self):
        return condition != config.unplayable_condition

    def kill(self):
        self.condition = config.unplayable_condition


mode = config.classic_mode
amount_players = int(input("Сколько игроков в игре? "))
amount_mafia = int(input("Сколько мафий в игре? "))
amount_doctors = 1
amount_detectives = 1
players = {}

if mode == config.configurate_mode:
    amount_doctors = int(input("Сколько докторов в игре? "))
    amount_detectives = int(input("Сколько детективов в игре? "))
total_players = list(range(1, amount_players + 1))
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


while all(mafia.is_alive() for mafia in players[config.mafia_key)]):
    pass