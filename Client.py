import threading
import socket


import threading
import socket


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print ("O usuário é um professor ou aluno?\n")
    username = input('Usuário> ')
    print('\nUsuario conectado!')

    if username == 'aluno': 
        print('\nBem vindo, aluno!')
        aluno = client #salva o endereço do cliente aluno para enviar a nota. 
        namefile = str(input('\nInsira o nome do arquivo que deseja enviar:'))
        print(namefile)
        client.send(namefile.encode('utf-8'))
        print("Arquivo enviado!")
        

    else : 
       print('Bem vindo, professor! Digite a nota do aluno:' )


    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

       


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()