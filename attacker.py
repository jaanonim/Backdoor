import socket

HOST = "127.0.0.1"
PORT = 7799


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Ready")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                toSend = input()
                conn.sendall(str.encode(toSend))

                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode())
    print("Disconnected")


if __name__ == "__main__":
    main()
