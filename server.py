import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso')

host = 'localhost'
port = 5432

s.bind((host, port)) ##ligação entre cliente servidor atraves do host e da porta
mensagem = '\nServidor: Oláaaaaa Cliente, e ai?'

while 1: ##se a ligação for verdadeira, receberá a resposta
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)