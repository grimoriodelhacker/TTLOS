from scapy.all import IP, ICMP, IPv6, ICMPv6EchoRequest, sr1 
import ipaddress

def determine_os(ip_address):
    try:
        # Verificar si la dirección IP es IPv4 o IPv6
        ip = ipaddress.ip_address(ip_address)

        if isinstance(ip, ipaddress.IPv4Address):
            # Enviar un paquete ICMPv4 con un TTL de 64
            packet = IP(dst=ip_address, ttl=64) / ICMP()
            response = sr1(packet, timeout=5, verbose=False)

            if response is None:
                print(f"No se recibió respuesta de {ip_address}")
                return

            # Analiza el TTL de la respuesta
            response_ttl = response.ttl
            print(f"TTL de la respuesta: {response_ttl}")

            if response_ttl >= 120:
                print(f"El dispositivo en {ip_address} probablemente es un Windows")
            elif response_ttl >= 60:
                print(f"El dispositivo en {ip_address} probablemente es un Linux o macOS")
            else:
                print(f"No se puede determinar el sistema operativo de {ip_address}")

        elif isinstance(ip, ipaddress.IPv6Address):
            # Enviar un paquete ICMPv6 con un TTL de 64
            packet = IPv6(dst=ip_address, hlim=64) / ICMPv6EchoRequest()
            response = sr1(packet, timeout=5, verbose=False)

            if response is None:
                print(f"No se recibió respuesta de {ip_address}")
                return

            # Analiza el TTL de la respuesta
            response_ttl = response.hlim
            print(f"TTL de la respuesta: {response_ttl}")

            if response_ttl >= 120:
                print(f"El dispositivo en {ip_address} probablemente es un Windows")
            elif response_ttl >= 60:
                print(f"El dispositivo en {ip_address} probablemente es un Linux o macOS")
            else:
                print(f"No se puede determinar el sistema operativo de {ip_address}")

        else:
            print(f"La dirección IP {ip_address} no es válida")

    except ValueError:
        print(f"La dirección IP {ip_address} no es válida")

if __name__ == "__main__":
    ip_address = input("Ingrese la dirección IP: ")
    determine_os(ip_address)
