import socket
import _thread

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "192.168.167.90"
port = 80

try:
    socketServer.bind((server, port))
except socket.error as error:
    print(error)

socketServer.listen(2)
print("Server started\nWait connected client")

SelectionsPleyers = ["", ""]

def threadClient(connection, numberPlayer):
    connection.send(str.encode(str(numberPlayer)))

    reply = ""
    while True:
        try:
            data = connection.recv(2048).decode()
            SelectionsPleyers[numberPlayer] = data
            print("Received from player" + str(numberPlayer) + ":", data)
            if not data:
                print("Disconnected")
                break
            else:
                if numberPlayer == 0:
                    while SelectionsPleyers[1] == "":
                        pass
                    reply = SelectionsPleyers[1]
                    SelectionsPleyers[1] = ""
                else:
                    while SelectionsPleyers[0] == "":
                        pass
                    reply = SelectionsPleyers[0]
                    SelectionsPleyers[0] = ""
                connection.sendall(str.encode(reply))

                print("Sending to pleyer" + str(numberPlayer) + ":", reply)
        except socket.error as error:
            print(error)
            break
    print("Lost connection")
    connection.close()

currentPlayer = 0
while True:
    (connection, address) = socketServer.accept()
    print("Connested to:", address)

    _thread.start_new_thread(threadClient, (connection, currentPlayer))
    currentPlayer += 1
