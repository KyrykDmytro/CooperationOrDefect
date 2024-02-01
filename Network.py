import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.167.90"
        self.port = 80
        #self.namePlayer = 
        self.Connect()
    
    def Connect(self):
        try:
            self.client.connect((self.server, self.port))
            return self.client.recv(2048).decode()
        except socket.error as error:
            print(error)

    def SendDate(self, date):
        try: 
            self.client.send(str.encode(date))
            return self.client.recv(2028).decode()
        except socket.error as error:
            print(error)
