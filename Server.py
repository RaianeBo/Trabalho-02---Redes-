import threading
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))
        server.listen()
        print ('Aguardando conexão do usuário!')
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        print("Conexão aceita:%s"%(addr[0]))

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

        namefile = client.recv(1024).decode()
        print(namefile)

        with open(namefile, 'wb') as file: 
            while 1: 
                data = client.recv(100000)
            if not data: 
                break 
            file.write(data)
        print(f'{namefile} recebido!\n')

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

main()