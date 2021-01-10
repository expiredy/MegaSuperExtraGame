import socket
import config
from main import player_choicing_window
from threading import Thread

# SERVER = '25.41.244.86'
SERVER =  socket.gethostname()
PORT = 9090



def listen():
    while True:
        try:
            in_data = client.recv(1024).decode()
            if in_data == config.choicing_key:
                print('Time To choice')
                player_choicing_window()
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

def run():
    client = socket.socket()
    client.connect((SERVER, PORT))
    print("Connected to server")

    thread_listen = Thread(target=listen)
    # thread_send = Thread(target=send)

    thread_listen.start()
    # thread_send.start()

    thread_listen.join()

if __name__ == '__main__':
    run()