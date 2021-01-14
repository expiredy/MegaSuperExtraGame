import config
import discord
import random
import string
import multiprocess
bot = None
passwords = []
bad_symbols = ['l', 'I', '1', '0', 'O', 'o']


class Server(discord.Client):
    def __init__(self, connection_type=config.connected_user):
        super().__init__()
        self.generated_key = None
        self.connection_type = connection_type
        self.id_of_room = None


    def check_room(self, key):
        return key in self.guild.channels

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

def connect(generated_key, next_func):
    pass