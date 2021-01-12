import config
import discord
import random
import string
passwords = []
bad_symbols = ['l', 'I', '1', '0', 'O', 'o']


class Server(discord.Client):
    def __init__(self, generated_key, connection_type=config.connected_user):
        super().__init__()
        self.generated_key = generated_key
        self.connection_type = connection_type
        self.id_of_room = None

    def check_room(self, key):
        return key in self.guild.channels

    async def on_ready(self):
        if self.connection_type == config.host_user:
            self.guild = self.get_guild(config.server_id)
            self.channel = await self.guild.create_text_channel(self.generated_key)
            self.channel.send(config.player_name + "connected")

    async def on_message(self, message):
        print(message)
        if message.channel.id == self.id_of_room:
            pass
        await message.channel.send('U suck')


def generate_key(len_of_password=6):
    key = ''
    while len_of_password > len(key):
        random_numbers = random.choice(list(string.ascii_letters))
        random_symbols = random.choice(list(string.digits))
        element = random.choice((random_numbers, random_symbols))
        if element not in bad_symbols:
            key += element
    if dont_already_used(key):
        return key
    else:
        return  generate_key()

def dont_already_used(key):
    return bot.check_room(key)

def activate(token, generated_key, connection_type=config.connected_user):
    global bot
    bot = Server(generated_key, connection_type)
    bot.run(token)

if __name__ == '__main__':
    activate(config.server_token, None)