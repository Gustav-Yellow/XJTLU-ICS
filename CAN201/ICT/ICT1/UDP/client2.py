# # client1 side
# import argparse
# import json
# import threading
# from socket import *
#
# class Client2:
#     def __init__(self, host, port):
#         self.server_host = host
#         self.server_port = port
#         self.sock = socket(AF_INET, SOCK_DGRAM)
#
#     # 接收信息
#     def receiving(self):
#         """接收服务器消息的线程"""
#         while True:
#             try:
#                 message, temp = self.sock.recvfrom(20480)
#                 message = message.decode()
#
#                 if message == "ask name":
#                     name = input("Enter your name: ")
#                     self.sock.sendto(name.encode(), (self.server_host, self.server_port))
#
#                 if message == "wait":
#                     print("Waiting for other players...")
#
#             except Exception as e:
#                 print("Error message: " + str(e))
#
#     def start(self):
#         print("Connected to server at " + self.server_host + ":" + str(self.server_port))
#         # 发送一条连接信息
#         self.sock.sendto("participate".encode(), (self.server_host, self.server_port))
#
#         self.receiving()
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description="This is description!")
#     parser.add_argument('--ip', action='store', required=True, dest='ip', help='The IP of server')
#     parser.add_argument('--port', action='store', required=True, dest='port', help='The port of server')
#     args = parser.parse_args()
#
#     # 游戏启动
#     game = Client2(args.ip, int(args.port))
#     game.start()
#
#

# client1 side
# client1 side
# client1 side
import argparse
import json
from socket import *

class Client:
    def __init__(self, host, port):
        self.server_host = host
        self.server_port = port
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.name = None

    # 接收信息
    def receiving(self):
        """接收服务器消息的线程"""
        while True:
            try:
                message, temp = self.sock.recvfrom(20480)
                message = json.loads(message)

                # 如果服务端请求名字
                if message['action'] == "ask name":
                    self.name = input("Enter your name: ")
                    self.sock.sendto(json.dumps({
                        "action": "participate",
                        "name": self.name
                    }).encode(), (self.server_host, self.server_port))

                # 如果服务端让等待
                if message['action'] == "wait":
                    print("Waiting for other players...")

                # 被告知游戏即将开始
                if message["action"] == "start game":
                    print("Game started!")

                # 发送猜测信息
                if message['action'] == "start guess":
                    print("Your turn to guess.")
                    guess = int(input("Enter your guess: "))
                    self.sock.sendto(json.dumps({
                        "action": "game",
                        "number": guess
                    }).encode(), (self.server_host, self.server_port))
                elif message["action"] == "wait for turn":
                    print("Waiting for your turn...")

                # 回答错误，继续等待
                if message["action"] == "wrong":
                    if "low" in message["message"]:
                        print("Your guess is too low.")
                        print("Waiting for your turn...")
                    else:
                        print("Your guess is too high.")
                        print("Waiting for your turn...")

                # 轮到你发信息了
                if message["action"] == 'your turn':
                    print(message["message"])
                    print("Your turn to guess.")
                    guess = int(input("Enter your guess: "))
                    self.sock.sendto(json.dumps({
                        "action": "game",
                        "number": guess
                    }).encode(), (self.server_host, self.server_port))

                # 消息正确
                if "winner" in message:
                    if message["action"] == "end" and message["winner"] == self.name:
                        print("Congratulations! You guessed the number!")
                        self.sock.close()
                        break
                    else:
                        print(message["winner"] + " guessed " + str(message["number"]) + " and won the game!")
                        self.sock.close()
                        break

            except Exception as e:
                print("Error message: " + str(e))

    def start(self):
        print("Connected to server at " + self.server_host + ":" + str(self.server_port))
        # 发送一条连接信息
        self.sock.sendto(json.dumps({
            "action": "participate",
            "name": None
        }).encode(), (self.server_host, self.server_port))

        self.receiving()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is description!")
    parser.add_argument('--ip', action='store', required=True, dest='ip', help='The IP of server')
    parser.add_argument('--port', action='store', required=True, dest='port', help='The port of server')
    args = parser.parse_args()

    # 游戏启动
    game = Client(args.ip, int(args.port))
    game.start()








