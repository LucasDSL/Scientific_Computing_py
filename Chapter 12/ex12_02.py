import socket
from urllib.parse import urlparse

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter url: ')
try: 
    components_url = urlparse(url)
    my_sock.connect((components_url.netloc, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    my_sock.send(cmd)
except: 
    print('Error - wrong or non existent url.')
    quit()
total_characters = 0
data_decoded = '' 
while True:
    data = my_sock.recv(512)
    if(len(data) < 1 or total_characters >= 3000):
        break 
    total_characters += len(data.decode())
    data_decoded += data.decode()
print(data_decoded[0:3000])
my_sock.close()