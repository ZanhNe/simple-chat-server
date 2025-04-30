import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.settimeout(1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)



connections = []
threads = []

def broadcast(connection: socket.socket, address: tuple):
    global connections
    while True:

        message = connection.recv(1024)
        if message.decode() == '0':
            break
        print(f"Received message from client {address}")
        for conn in connections:
            if connection != conn['connection']:
                conn['connection'].sendall(message)

    for conn in connections:
        if connection == conn['connection']:
            connections.remove(conn)
    
    connection.close()

    

while True:
    try:
        connection, address = server_socket.accept()
        connections.append({'connection': connection, 'address': f"{address[0]}:{address[1]}"})
        thread = threading.Thread(target=broadcast, args=(connection, address), daemon=True)
        thread.start()

    except socket.timeout:
        continue


