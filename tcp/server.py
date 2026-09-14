import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server akan berjalan di semua alamat IP yang tersedia
host = "0.0.0.0"
port = 12345

server.bind((host, port))
server.listen()
print(f"Server listening on {host}:{port}")

# Menerima koneksi dari client
client_socket, address = server.accept()
print(f"Koneksi diterima dari {address}")

# Menerima pesan dari client
pesan = client_socket.recv(1024).decode("utf-8")
print(f"Pesan dari client: {pesan}")

# Mengirim balasan ke client
balasan = "ping"
client_socket.send(balasan.encode("utf-8"))

# Menutup koneksi
client_socket.close()
server.close()
