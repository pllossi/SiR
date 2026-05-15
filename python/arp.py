import time
from scapy.all import Ether, ARP, sendp

print("=== AVVIO SIMULAZIONE SCAMBIO ARP ===")

# IP e MAC inventati per il test
PC_MAC = "aa:bb:cc:dd:ee:ff"
PC_IP  = "192.168.1.5"

ROUTER_MAC = "11:22:33:44:55:66"
ROUTER_IP  = "192.168.1.1"

# 1. LA RICHIESTA (ARP Request)
# Il PC chiede a TUTTI (Broadcast) chi ha l'IP del router
richiesta = Ether(src=PC_MAC, dst="ff:ff:ff:ff:ff:ff") / \
            ARP(op=1, hwsrc=PC_MAC, psrc=PC_IP,
                hwdst="00:00:00:00:00:00", pdst=ROUTER_IP)

sendp(richiesta) # Usa 'lo' su Linux/Mac o ometti su Windows
print("[1/2] ARP Request inviato in Broadcast...")

time.sleep(1) # Pausa di 1 secondo per separare i pacchetti

# 2. LA RISPOSTA (ARP Reply)
# Il Router risponde DIRETTAMENTE al PC (Unicast)
risposta = Ether(src=ROUTER_MAC, dst=PC_MAC) / \
           ARP(op=2, hwsrc=ROUTER_MAC, psrc=ROUTER_IP,
               hwdst=PC_MAC, pdst=PC_IP)

sendp(risposta)
print("[2/2] ARP Reply inviato in Unicast!")
print("=== SIMULAZIONE COMPLETATA ===")