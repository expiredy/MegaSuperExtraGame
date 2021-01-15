import config
import discord
import random
import string
import asyncio
import multiprocess
bot = None
passwords = []
bad_symbols = ['l', 'I', '1', '0', 'O', 'o']


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
    def __init__(self, connection_type=config.connected_user):
        super().__init__()
        self.generated_key = None
        self.connection_type = connection_type
        self.id_of_room = None


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
            await self.channel.send(config.player_name + " connected")

    async def on_message(self, message):
        print(message)
        if message.channel.id == self.id_of_room:
            if self.connection_type == config.host_user:
                if message.content.startswith(config.connected_event):
                    pass
                elif message.content.split()[0].isdigit():
                    pass



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


def activate(token, connection_type=config.connected_user):
    global bot
    bot = Server(connection_type)
    bot.run(token)

def create():
    new_thread = multiprocess.Process(target=activate, args=(config.server_token, config.host_user))
    new_thread.start()
    return

def connect(generated_key):
    new_thread = multiprocess.Process(target=activate, args=(config.server_token, config.connected_user))
    new_thread.start()
    return

def waiting_for_connection(text):
    global bot
    while not bot:
        pass
    send(text)

def send(text):
    global bot
    if bot:
        ioloop = asyncio.get_event_loop()
        print(ioloop)
        new_task = ioloop.create_task(bot.sender(text))
        asyncio.wait(new_task)
        ioloop.run_until_complete(wait_tasks)
        ioloop.close()
    else:
        wait_for_connecntion = multiprocess.Process(target=waiting_for_connection, args=(text, ))
        wait_for_connecntion.start()