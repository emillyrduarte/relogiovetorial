import socket

HOST = 'localhost' 
PORT = 12345 

clock = [0, 0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Digite o cartao sus (ou "sair" para sair): ')
        if message == 'sair':
            break
        clock[1] += 1
        message_clock = ','.join(str(x) for x in clock)
        message = message_clock + ':' + message
        s.sendall(message.encode('utf-8'))
        data = s.recv(1024)
        message_clock, message = data.decode('utf-8').split(':')
        message_clock = [int(x) for x in message_clock.split(',')]
        clock = [max(clock[i], message_clock[i]) for i in range(len(clock))]
        print('Data da consulta:', data.decode('utf-8'))
