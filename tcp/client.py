import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Luis
# server_host = "10.7.101.79"

# Abdul
server_host = "10.7.101.141"

server_port = 12345
client.connect((server_host, server_port))
print(f"Terhubung ke server di {server_host}:{server_port}")

# # Mengirim pesan ke server
# pesan = "halo biniku shinobu aku cinta sampe mati karena kamu ungu lovvv"
# client.send(pesan.encode("utf-8"))

# # Menerima balasan dari server
# balasan = client.recv(1024).decode("utf-8")
# print(f"Balasan dari server: {balasan}")

while True:
    # Mengirim pesan ke server
    pesan = input("Masukkan pesan untuk server (ketik 'exit' untuk keluar): ")
    if pesan.lower() == "exit":
        break
    client.send(pesan.encode("utf-8"))

    # Menerima balasan dari server
    balasan = client.recv(1024).decode("utf-8")
    print(f"Balasan dari server: {balasan}")

# Menutup koneksi
client.close()
