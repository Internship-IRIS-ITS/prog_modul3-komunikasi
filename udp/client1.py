# Client: Alice

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bob_address = ("localhost", 12345)
alice_address = ("localhost", 54321)

sock.bind(alice_address)

print("Alice udah online nih!")

while True:
    msg = input("Alice: ")
    sock.sendto(msg.encode("utf-8"), bob_address)

    sock.settimeout(0.1)

    try:
        data, addr = sock.recvfrom(1024)
        print(f"Bob {addr}: {data.decode('utf-8')}")
    except socket.timeout:
        pass
    except KeyboardInterrupt:
        print("\nAlice dihentikan")
    finally:
        sock.close()
