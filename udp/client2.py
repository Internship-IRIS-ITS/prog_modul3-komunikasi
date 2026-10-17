# Client: Bob

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bob_address = ("10.7.101.138", 12345)
alice_address = ("<IP-TARGET>", 54321)

# bind ke semua interface, port sendiri
sock.bind(("0.0.0.0", bob_address[1]))

print("Bob sudah online nih!")


def receive():
    while True:
        try:
            data, addr = sock.recvfrom(4096)
        except OSError:  # socket sudah ditutup
            break
        print(f"\nAlice {addr}: {data.decode()}\nBob: ", end="", flush=True)


threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        msg = input("Bob: ")
        sock.sendto(msg.encode(), alice_address)
except (KeyboardInterrupt, EOFError):
    print("\nBob dihentikan")
finally:
    sock.close()
