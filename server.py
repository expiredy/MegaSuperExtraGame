import socket
from threading import Thread

LOCALHOST = '25.41.244.86'
PORT = 9090
server = socket.socket()
server.bind((LOCALHOST, PORT))
server.listen(1)

print('Server started...')
clientConnection, clientAddress = server.accept()
print('Connected client:', clientAddress)
msg = ''


def listen():
    while True:
        try:
            in_data = clientConnection.recv(1024)
            message = in_data.decode()
            if message == 'bye':
                break
            print(f'From client: {message}')
        except socket.error:
            print("Lost connection to client [L]")
            clientConnection.close()
            break


def send():
    while True:
        try:
            out_data = input()
            clientConnection.send(bytes(out_data, 'UTF-8'))
        except socket.error:
            print("Lost connection to client [S]")
            clientConnection.close()
            break


thread_listen = Thread(target=listen)
thread_send = Thread(target=send)

thread_listen.start()
thread_send.start()

thread_listen.join()
thread_send.join()