import argparse
import json
from socket import *


class Client:
    def __init__(self, host, port):
        self.server_host = host
        self.server_port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.server_host, self.server_port))
        self.name = None

    # 启动监听
    def receiving(self):
        """Receives messages from the server continuously."""
        buffer = ""
        try:
            while True:
                data = self.sock.recv(2048).decode()
                if not data:
                    break
                buffer += data

                while '\n' in buffer:
                    message, buffer = buffer.split('\n', 1)
                    message = json.loads(message)
                    self.handle_message(message)
        except Exception as e:
            print("Error message: " + str(e))
            self.sock.close()

    # 处理接收到的信息
    def handle_message(self, message):
        """Handles server messages."""
        if message['action'] == "ask name":
            self.name = input("Enter your name: ")
            self.sock.send((json.dumps({
                "action": "participate",
                "name": self.name
            }) + "\n").encode())

        # 等待其他人加入
        elif message['action'] == "wait":
            print("Waiting for other players...")

        # 游戏正式开始
        elif message["action"] == "start game":
            print("Game started!")

        # 第一轮从你开始去猜数字
        elif message['action'] == "start guess":
            print("Your turn to guess.")
            self.input_legal_num()

        # 等待别人猜数字
        elif message["action"] == "wait for turn":
            print(f'{message["message"]}')
            print("Waiting for your turn...")


        # 到你的回合猜数字
        elif message["action"] == 'your turn':
            print(message["message"])
            self.input_legal_num()

        # 你是胜利者
        elif "winner" in message:
            if message["action"] == "end" and message["winner"] == self.name:
                print(f"Congratulations! You guessed the number!")
            else:
                print(f"{message['winner']} guessed {message['number']} and won the game!")
            self.sock.close()

    # 确保用户输入合法的数字
    def input_legal_num(self):
        while True:
            try:
                # 获取用户输入并转换为整数
                guess = int(input("Enter your guess (1-100): "))

                # 检查数字是否在范围内
                if 1 <= guess <= 100:
                    # 如果输入有效，发送数据并结束循环
                    self.sock.send((json.dumps({
                        "action": "game",
                        "number": guess
                    }) + "\n").encode())
                    return guess  # 退出循环
                else:
                    print("Invalid input. Please enter a number between 1 and 100.")

            except ValueError:
                # 捕捉到非数字输入错误
                print("Invalid input. Please enter a valid number.")

    def start(self):
        print(f"Connected to server at {self.server_host}:{self.server_port}")
        # Send initial participation message
        self.sock.send((json.dumps({
            "action": "participate",
            "name": None
        }) + "\n").encode())
        self.receiving()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is description!")
    parser.add_argument('--ip', action='store', required=True, dest='ip', help='The IP of server')
    parser.add_argument('--port', action='store', required=True, dest='port', help='The port of server')
    args = parser.parse_args()

    # Start the game
    game = Client(args.ip, int(args.port))
    game.start()
