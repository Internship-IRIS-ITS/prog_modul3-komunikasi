# Client: Bob

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bob_address = ("localhost", 12345)
alice_address = ("localhost", 54321)

sock.bind(bob_address)

print("Bob sudah online nih!")

while True:
    msg = input("B: ")
    sock.sendto(msg.encode(), alice_address)

    sock.settimeout(0.1)
    try:
        data, addr = sock.recvfrom(4096)
        print(f"Alice {addr}:", data.decode())
    except socket.timeout:
        pass
    except KeyboardInterrupt:
        print("\nBob dihentikan")
    finally:
        sock.close()
