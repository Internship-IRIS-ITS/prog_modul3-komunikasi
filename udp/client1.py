# Client: Alice

import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bob_address = ("<IP-TARGET>", 12345)
alice_address = ("10.7.101.138", 54321)

# bind ke semua interface, port sendiri
sock.bind(("0.0.0.0", alice_address[1]))

print("Alice udah online nih!")


def receive():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
        except OSError:  # socket sudah ditutup
            break
        print(f"\nBob {addr}: {data.decode('utf-8')}\nAlice: ", end="", flush=True)


threading.Thread(target=receive, daemon=True).start()

try:
    while True:
        msg = input("Alice: ")
        sock.sendto(msg.encode("utf-8"), bob_address)
except (KeyboardInterrupt, EOFError):
    print("\nAlice dihentikan")
finally:
    sock.close()
