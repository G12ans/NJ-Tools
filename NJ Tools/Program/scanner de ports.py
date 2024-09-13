import socket

def scan_ports(ip, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on {ip}")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

ip = "88.124.228.21"  # Adresse IP de la cible (à remplacer par celle que tu veux scanner)
start_port = 1
end_port = 1024
scan_ports(ip, start_port, end_port)
