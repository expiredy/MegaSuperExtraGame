import config
import discord
import random
import string
import asyncio
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
    def __init__(self, connection_type=config.connected_user):
        super().__init__()
        waiting_for_start = Thread(target=self.__checking_for_start)
        waiting_for_start.start()
        self.generated_key = None
        self.connection_type = connection_type
        self.id_of_room = None

    def __checking_for_start(self):
        pass

    def check_room(self, key):
        return key in self.guild.channels

    async def sender(self, text):
        await self.get_channel(self.id_of_room).send(text)

    async def on_ready(self):
        self.generated_key = generate_key()
        if self.connection_type == config.host_user:
            self.guild = self.get_guild(config.server_id)
            self.channel = await self.get_channel(config.main_room_id).clone(name=self.generated_key, reason=None)
            self.id_of_room = self.channel.id
            await self.channel.send(config.give_info())
            await self.channel.send(config.player_name + " connected")

    async def on_message(self, message):
        print(message)

        if message.channel.id == self.id_of_room:
            if self.connection_type == config.host_user:
                if message.content.split(self.separator)[0] == config.connected_event:
                    player_data = message.content.split(self.separator)
                    new_player = Player(total_members.keys())
                elif message.content.split(self.separator)[0] == config.dead_event:
                    pass
                elif message.content.split(self.separator)[0] == config.vote_event:
                    pass
            if message.content.split(self.separator)[0] == config.game_start_event:
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


def activate(token):
    global role
    role = config.host_user
    config.server = Server(role)
    config.server.run(token)


def create():
    global new_thread, role
    role = config.host_user

    new_thread = multiprocess.Process(target=activate, args=(config.server_token, ))
    new_thread.start()
    return

def connect(generated_key):
    global new_thread, role
    role = config.connected_user
    new_thread = multiprocess.Process(target=activate, args=(config.server_token, config.server))
    new_thread.start()
    config.server = new_thread.get()
    return

def exit_from_server():
    print("SICK")
    try:
        new_thread.join()
        print('SUCK')
        return
    except:
        return

def send(text):
    print(config.server)
    if config.server:
        ioloop = asyncio.get_event_loop()
        print(ioloop)
        new_task = ioloop.create_task(config.server.sender(text))
        asyncio.wait(new_task)
        ioloop.run_until_complete(new_task)
        ioloop.close()