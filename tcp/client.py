import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menghubungkan ke server
server_host = "127.0.0.1"
server_port = 12345
client.connect((server_host, server_port))
print(f"Terhubung ke server di {server_host}:{server_port}")

# Mengirim pesan ke server
pesan = "Halo server, ini pesan dari client!"
client.send(pesan.encode("utf-8"))

# Menerima balasan dari server
balasan = client.recv(1024).decode("utf-8")
print(f"Balasan dari server: {balasan}")

# Menutup koneksi
client.close()
