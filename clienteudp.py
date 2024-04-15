import socket #biblioteca importante para redes, segurança, udp contempla principio de disponibilidade

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##UDP protocolo de datagrama do usuário

print('Cliente Socket Criado com sucesso!!!')

host = 'localhost' ##rede local, interna da sua máquina
porta = 5433
mensagem = 'Olá servidor firmeza?'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) ##vai enviar uma mensagem pro servidor e aguardar uma resposta

    dados, servidor = s.recvfrom(4096) ##vai receber uma mensagem do servidor de 4096b
    dados =  dados.decode() ##vai desempacotar os dados e mostrar o resultado abaixo
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close() ##fecha a conexão para não ficar em loop