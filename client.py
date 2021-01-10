import socket
import config
from threading import Thread

# SERVER = '25.41.244.86'
SERVER =  socket.gethostname()
PORT = 9090

client = socket.socket()
client.connect((SERVER, PORT))
print("Connected to server")


def listen():
    while True:
        try:
            in_data = client.recv(1024).decode()
            if in_data == config.choicing_key:
                print('Time To choice')
            print('From server:', in_data)
        except socket.error:
            print('Lost connection to server [L]')
            client.close()
            break


def send(out_data):
    while True:
        try:
            client.sendall(bytes(out_data, 'UTF-8'))
            if out_data == 'bye':
                break
        except socket.error:
            print('Lost connection to server [S]')
            client.close()
            break


thread_listen = Thread(target=listen)
# thread_send = Thread(target=send)

thread_listen.start()
# thread_send.start()

thread_listen.join()