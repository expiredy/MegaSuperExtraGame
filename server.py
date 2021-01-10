import socket
import random
import config
from threading import Thread

server_is_active = True
# LOCALHOST = '25.41.244.86'
LOCALHOST =  socket.gethostname()
PORT = 9090
server = socket.socket()
server.bind((LOCALHOST, PORT))
server.listen(10)
server_members = {}
print('Server started...')
connected_players = {}

class Player:
    def __init__(self, id, name=random.choice(config.ExtraTHICCnames), role=None, avatar=None,
                 condition=config.normal_condition):
        self.id, self.name, self.role, self.condition = id, name, role, condition
        self.avatar = avatar

    def set_role(self, new_role):
        self.role = new_role

    def get_role(self):
        return self.role

    def send(self, data):
        return send_to_client(data)

    def is_alive(self):
        return condition != config.unplayable_condition

    def make_viewer(self):
        self.condition = config.unplayable_condition

    def awake(self):
        self.condition = config.condition_for_sleep

    def __str__(self):
        return name

def conection():
    global server_is_active
    while server_is_active:
        clientConnection, clientAddress = server.accept()
        server_members[len(list(server_members.keys()))] = {config.connection_key: clientConnection,
                                                            config.address_key: clientConnection,
                                                            config.listener_key: Thread(target=send_to_client,
                                                                                        args=
                                                                                        (len(list(server_members
                                                                                                  .keys())),)),
                                                            config.sender_key: Thread(target=listen,
                                                                                      args=
                                                                                      (len(list(server_members
                                                                                                .keys())), ))
                                                            }
        server_members[len(list(server_members.keys())) - 1][config.listener_key].start()
        server_members[len(list(server_members.keys())) - 1][config.sender_key].start()
        print('Connected client:', clientAddress)


def listen(id):
    global server_is_active
    clientConnection = server_members[id][config.connection_key]
    while server_is_active:
        try:
            in_data = clientConnection.recv(1024)
            message = in_data.decode()
            if message == sonfig.disconect_message:
                break
            return message
        except socket.error:
            print("Lost connection to client [L]")
            clientConnection.close()
            break

def send(out_data):
    global server_is_active
    try:
        clientConnection.send_to_client(bytes(out_data, 'UTF-8'))
    except socket.error:
        print("Lost connection to client [S]")
        clientConnection.close()

def send_to_client(id):
    pass

def choicing_player(key):
    for player in list(server_members.keys()):
        if server_members[player] == key:
            player_id = player.send_to_client(config.choicing_key)

def night_script():
        choicing_player(config.mafia_key)
        choicing_player(config.doctor_key)
        choicing_player(config.detective_key)


def morninig_script():
    pass


def day_script():
    choicing_player(config.inhabitants_key)



def main():
    thread_connecting = Thread(target=conection)
    thread_connecting.start()

    mode = config.classic_mode
    amount_players = int(input("Сколько игроков в игре? "))
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
        for player in range(len(players[config.classic_order[key]])):
            print(player, 'is', config.classic_order[key])


    while all([total_players[mafia].is_alive() for mafia in total_players[config.mafia_key]]):
        night_script()
        morninig_script()
        day_script()


    thread_connecting.join()
    thread_listen.join()
    thread_send.join()

if __name__ == '__main__':
    main()