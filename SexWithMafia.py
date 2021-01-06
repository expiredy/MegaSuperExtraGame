import random
import config
players = {}

class Player:
    def __init__(self, id, name, role=None, condition=config.normal_condition):
        self.id, self.name, self.role, self.condition = id, name, role, condition

    def set_role(self, new_role):
        self.role = new_role

    def kill(self):
        self.condition = config.unplayable_condition

mode = 'classic'
amount_players = int(input("Сколько игроков в игре? "))
amount_mafia = int(input("Сколько мафий в игре? "))
players = list(range(1, amount_players + 1))
random.shuffle(players)
mafia = [players.pop() for _ in range(amount_mafia)]
doctor = players.pop()
detective = players.pop()
if mode != 'classic':
    pass
inhabitants = players


print("Мафией(ями) являются игроки:", *mafia)
print("Доктором является игрок:", doctor)
print("Детективом является игрок:", detective)
print("Мирные жители:", *inhabitants)



while mafia:
    pass