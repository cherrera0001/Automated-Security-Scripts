from scapy.all import ARP, Ether, srp
import nmap

def scan_network(ip_range):
    print(f"Escaneando la red en el rango {ip_range}...")

    # Crear paquete ARP
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Enviar paquete ARP y recibir respuestas
    result = srp(packet, timeout=3, verbose=0)[0]

    # Lista de dispositivos descubiertos
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def scan_ports(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, '1-1024')  # Escanea los primeros 1024 puertos

    print(f"\nPuertos abiertos para {ip}:")
    for proto in scanner[ip].all_protocols():
        lport = scanner[ip][proto].keys()
        for port in lport:
            print(f"Port {port}: {scanner[ip][proto][port]['state']}")

if __name__ == "__main__":
    ip_range = input("Ingrese el rango de IP a escanear (ej. 192.168.1.0/24): ")
    devices = scan_network(ip_range)
    
    if devices:
        print("\nDispositivos detectados:")
        for device in devices:
            print(f"IP: {device['ip']} \t MAC: {device['mac']}")
            
        scan_choice = input("\n¿Quieres escanear los puertos de los dispositivos encontrados? (s/n): ")
        if scan_choice.lower() == 's':
            for device in devices:
                scan_ports(device['ip'])
    else:
        print("No se detectaron dispositivos.")
