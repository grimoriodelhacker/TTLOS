# IP OS Detector

IP OS Detector es una herramienta creada para determinar el sistema operativo de un dispositivo a partir de su dirección IP. Este código funciona con IPv4 e IPv6. La herramienta se basa en la librería Scapy y utiliza el valor TTL (Time To Live) de las respuestas ICMP para inferir el sistema operativo.

## Características

- **Determinación de Sistema Operativo**: Envía paquetes ICMP a direcciones IPv4 e IPv6 y analiza el TTL de la respuesta para determinar el sistema operativo del dispositivo.
- **Soporte para IPv4 e IPv6**: La herramienta puede manejar tanto direcciones IPv4 como IPv6.

## Requisitos

- Python 3.x
- Librería Scapy

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/IP-OS-Detector.git
   cd IP-OS-Detector

2. Instala las dependencias:
```sh
pip install scapy
pip install ipaddress
