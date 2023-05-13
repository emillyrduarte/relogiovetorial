import socket
import random
from datetime import date

HOST = ''  
PORT = 12345  

clock = [0, 0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Aguardando conexões...')
    conn, addr = s.accept()  
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024) 
            message_clock, message = data.decode('utf-8').split(':')
            message_clock = [int(x) for x in message_clock.split(',')]
            clock = [max(clock[i], message_clock[i]) for i in range(len(clock))]
            clock[0] += 1
            message_clock = ','.join(str(x) for x in clock)
            message = (date(2023,random.randint(1,12),random.randint(1,30))).strftime("%d/%m/%Y")
            
            conn.sendall((message_clock + ':' + message).encode('utf-8'))
