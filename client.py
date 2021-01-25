import socket
import config
from threading import Thread

# SERVER = '25.41.244.86'
SERVER =  socket.gethostname()
PORT = 9090
separator = ' '
grouper = '"'
all_players = {}


def listen():
    global client
    while True:
        try:
            in_data = client.recv(1024)
            message = in_data.decode()
            print('From server:', in_data)
            event = message.split(self.separator)[0]
            content = [message[i + 1:message[i + 1:].find(self.grouper)]
                       for i in range(len(message)) is sybol == self.grouper and i + 1 <= len(message)
                       and ''.join(message[i:message[i + 1:].find(self.grouper)].split())]
            print(content)
            if config.message_to_send:
                send(separator.join([config.chat_event, config.id, grouper + config.message_to_send + grouper]))
                config.message_to_send = None

            if event == config.change_info_event:
                content[0]
            elif event == config.got_mail_event:
                config.chat_history[len(list(config.chat_history.keys()))] = {config.author_key: config.players[id],
                                                                              config.context_key: content[1]}

        except socket.error:
            print('Lost connection to server [L]')
            client.close()
            break


def send(out_data):
    global client
    try:
        client.sendall(bytes(out_data, 'UTF-8'))
        if out_data == 'bye':
            exit()
    except socket.error:
        print('Lost connection to server [S]')
        client.close()

def run(server_id):
    global client
    client = socket.socket()
    client.connect((server_id, PORT))
    print("Connected to server")

    thread_listen = Thread(target=listen)

    thread_listen.start()

    thread_listen.join()

if __name__ == '__main__':
    run('localhost')