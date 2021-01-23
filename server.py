import socket
import config
import random
import string
import asyncio
import time
import os
from threading import Thread


class Server:
    separator = ' '
    server_members = {}
    def __init__(self, LOCALHOST='localhost'):
        PORT = 9090
        config.accepting = True
        self.server = socket.socket()
        self.server.bind((LOCALHOST, PORT))
        self.server.listen(2)

        self.accepting = Thread(target=self.accept_players)
        self.thread_listen = Thread(target=self.listen)
        self.thread_send = Thread(target=self.send)

        self.thread_listen.start()
        self.thread_send.start()
        self.accepting.start()


        print('Server started...')

    def accept_players(self):
        while config.accepting:
            clientConnection, clientAddress = self.server.accept()
            print('Connected client:', clientAddress)
            self.server_members[len(list(self.server_members.keys()))] = {config.connection_key: clientConnection,
                                                                          config.address_key: clientAddress,
                                                                          config.listener_key: None,
                                                                config.sender_key: None,
                                                                config.role_key: None
                                                                }


    def end_sesion(self):
        self.thread_listen.join()
        self.thread_send.join()
        self.accepting.join()

    def listen(self):
        while True:
            try:
                in_data = clientConnection.recv(1024)
                message = in_data.decode()
                if message.split(self.separator)[0] == config.connected_event:
                    player_data = message.content.split(self.separator)
                    new_player = Player(total_members.keys())
                    self.total_players[len(list(self.total_players.keys()))] = new_player

                elif message.split(self.separator)[0] == config.dead_event:
                    pass
                elif message.split(self.separator)[0] == config.vote_event:
                    pass
                if message == 'bye':
                    break
                print(f'From client: {message}')
            except socket.error:
                print("Lost connection to client [L]")
                clientConnection.close()
                break


    def send(self):
        for connection in [self.server_members[key][config.connection_key] for key in list(self.server_members.keys())
                           if self.server_members[key][config.role_key] != config.viewer_key]:
            try:
                connection.send(bytes(out_data, 'UTF-8'))
            except socket.error:
                print("Lost connection to client [S]")
                clientConnection.close()

class Player:
    def __init__(self, id, name=random.choice(config.ExtraTHICCnames), role=None, avatar=None,
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






if __name__ == '__main__':
    created_server = Server()