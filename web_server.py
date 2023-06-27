import network
import socket
from time import sleep

ssid = '' # Enter wifi name
password = '' # Enter wifi password

def connect():
    # Connect to WiFi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    html = f"""
        <!doctype html>
        <html>
        <head>
        <title>Demo page</title>
        </head>
        <body>
        <h1>Hello, world!</h1>
        </body>
        </html>
    """
    return str(html)

def serve(connection):
    client = connection.accept()[0]
    request = client.recv(1024)
    request = str(request)
    html = webpage()
    client.send(html)
    client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
