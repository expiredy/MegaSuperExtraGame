import config
import discord
import random
import string
import asyncio
import time
import os
import multiprocess
from threading import Thread
from multiprocess import Process, Lock
server = None
passwords = []
role = None
new_thread = None
bad_symbols = ['l', 'I', '1', '0', 'O', 'o']
total_members = {}


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


class Server(discord.Client):
    separator = ' '
    def __init__(self, key, connection_type=config.connected_user):
        super().__init__()
        self.waiting_for_start = Thread(target=self.__checking_for_start)
        self.waiting_for_start.start()
        self.generated_key = key
        self.total_players = {}
        self.connection_type = connection_type
        self.id_of_room = None

    def __checking_for_start(self):
        while True:
            time.sleep(1)
            with open(config.launch_path, 'r+') as f:
                read_data = f.read().split('\n')[0]
                print(read_data)
                if eval(read_data):
                    config.game_start_event = True
                    break

    async def sender(self, text):
        await self.get_channel(self.id_of_room).send(text)

    async def on_ready(self):
        self.guild = self.get_guild(config.server_id)
        self.channel = None
        if self.connection_type == config.host_user:
            self.generated_key = generate_key()
            self.channel = await self.get_channel(config.main_room_id).clone(name=self.generated_key, reason=None)
        else:
            for channel in self.guild.channels:
                if channel.name == self.generated_key:
                    self.channel = channel
        self.id_of_room = self.channel.id
        await self.channel.send(config.connected_event + self.separator + config.give_info())

    async def on_message(self, message):
        print(message)

        if message.channel.id == self.id_of_room:
            if self.connection_type == config.host_user:
                if message.content.split(self.separator)[0] == config.connected_event:
                    player_data = message.content.split(self.separator)
                    new_player = Player(total_members.keys())
                    self.total_players[len(list(self.total_players.keys()))] = new_player

                elif message.content.split(self.separator)[0] == config.dead_event:
                    pass
                elif message.content.split(self.separator)[0] == config.vote_event:
                    pass
            if message.content.split(self.separator)[0] == config.game_start_event:
                if self.connection_type == config.host_user:
                    self.amount_players = len(list(self.total_players.keys()))
                    players = list(range(0, amount_pslayers))
                    random.shuffle(players)
                    for _ in range(config.amount_mafia):
                        self.total_players[players.pop()].set_role(config.mafia_key)
                    for _ in range(config.amount_doctors):
                        self.total_players[players.pop()].set_role(config.doctor_key)
                    for _ in range(config.amount_detectives):
                        self.total_players[players.pop()].set_role(config.detective_key)
                    if mode != config.classic_mode:
                        pass
                    for _ in range(len(players)):
                        self.total_players[players.pop()].set_role(config.inhabitants_key)
                    for people in self.total_players:
                        await self.channel.send()
                else:
                    pass

            elif message.content.split(self.separator)[0] == config.message_sended:
                print(message.content)
            elif message.content.split(self.separator)[0] == config.player_choiced:
                pass
            elif message.content.split(self.separator)[0] == config.game_over:
                pass
            # elif message.content.split(self.separator)[0] == config.t_event:
            #     pass



def generate_key(len_of_password=6):
    key = ''
    while len_of_password > len(key):
        random_numbers = random.choice(list(string.ascii_letters))
        random_symbols = random.choice(list(string.digits))
        element = random.choice((random_numbers, random_symbols))
        if element not in bad_symbols:
            key += element
    print(key)
    return ''.join(key.lower().split())


def create():
    global new_thread
    role = config.host_user
    return

def connect(generated_key):
    global new_thread
    role = config.connected_user
    return
