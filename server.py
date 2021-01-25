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
    grouper = '"'
    server_members = {}
    def __init__(self, LOCALHOST='localhost'):
        PORT = 9090
        config.accepting = True
        self.server = socket.socket()
        self.server.bind((LOCALHOST, PORT))
        self.server.listen(2)

        self.accepting = Thread(target=self.accept_players)
        self.thread_send = Thread(target=self.sending)

        self.thread_send.start()
        self.accepting.start()


        print('Server started...')

    def accept_players(self):
        while config.accepting:
            clientConnection, clientAddress = self.server.accept()
            print('Connected client:', clientAddress)
            self.server_members[len(list(self.server_members.keys()))]\
                = {config.connection_key: clientConnection, config.address_key: clientAddress,
                   config.listener_key: Thread(target=self.listen, args=(clientConnection,)),
                   config.sender_key: None,
                   config.role_key: None}
            self.server_members[len(list(self.server_members.keys()))][config.listener_key].start()
            self.sending(
                self.separator.join([config.change_info_event, str(len(list(self.server_members.keys())) - 1)]))

    def end_sesion(self):
        self.thread_listen.join()
        self.accepting.join()

    def listen(self, clientConnection):
        while config.listen_players:
            try:
                in_data = clientConnection.recv(1024)
                message = in_data.decode()
                event = message.split(self.separator)[0]
                content = [message[i + 1:message[i + 1:].find(self.grouper)]
                           for i in range(len(message)) is sybol == self.grouper and i + 1 <= len(message)
                           and ''.join(message[i:message[i + 1:].find(self.grouper)].split())]
                print(content)
                id = message.split(self.separator)[1]

                if event == config.change_info_event:
                    self.sending(separator.join([config.change_info_event, id,]))
                elif event == config.vote_event:
                    pass
                elif event == config.dead_event:
                    pass
                elif event == config.chat_event:
                    self.sending(message)

                if message == 'bye':
                    break
                print(f'From client: {message}')
            except socket.error:
                print("Lost connection to client [L]")
                clientConnection.close()
                break


    def sending(self, out_data, default_connection=None):
        if not default_connection:
            for connection in [self.server_members[key][config.connection_key] for key in list(self.server_members.keys())
                               if self.server_members[key][config.role_key] != config.viewer_key]:
                try:
                    connection.send(bytes(out_data, 'UTF-8'))
                except socket.error:
                    print("Lost connection to client [S]")
                    connection.close()
        else:
            try:
                default_connection.send(bytes(out_data, 'UTF-8'))
            except socket.error:
                print("Lost connection to client [S]")
                default_connection.close()



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

def mafia_time():
    pass
def healing_time():
    pass
def detective_time():
    pass
def show_results():
    pass
def voiting():
    pass

def end_game():
    print("Ha-ha noone won cause game aren't ended")

def main_game():
    while any([config.players[role_key].is_alive() for role_key in list(config.players.keys())
               if config.players[role_key].role == config.mafia_key]):
        mafia_time()
        healing_time()
        detective_time()
        show_results()
        voiting()
    end_game()



if __name__ == '__main__':
    created_server = Server()