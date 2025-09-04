import argparse
import json
import random
import time
from socket import *
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.player_num = 2  # 这里可以调整想要参加这个游戏的人数，默认为2
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.player_num)
        self.target_number = random.randint(1, 100)
        self.clients = []  # (client_socket, client_address, client_name)
        self.current_guesser = 0
        self.sequence = []  # 存储每个用户与结果的差值  [[client_name1, index], [client_name2, index]]
        self.game_over = False

    # 处理接收到的client请求
    def handle_client(self, client_sock, client_address):
        # 防止tcp粘包
        buffer = ""
        while not self.game_over:
            try:
                data = client_sock.recv(2048).decode()
                if not data:
                    break
                buffer += data

                while '\n' in buffer:
                    message, buffer = buffer.split('\n', 1)
                    data = json.loads(message)
                    if data["action"] == 'participate':
                        self.participant_action(data, client_sock, client_address)
                    elif data["action"] == 'game':
                        self.judge_number(data, client_sock)
            except Exception as e:
                print("Error message: " + str(e))
                break
        client_sock.close()

    # 处理新到来的client
    def participant_action(self, data, client_sock, client_address):
        if data['name'] is None:
            print(f"Client connected: {client_address[0]}:{client_address[1]}")
            client_sock.send((json.dumps({
                "action": "ask name"
            }) + "\n").encode())
        else:  # 如果此时返回的结果中有名字，则保存到当前的clients中
            self.clients.append((client_sock, client_address, data["name"]))
            # 首轮添加的时候，按照先后注入的顺序，用数组保存
            self.sequence.append([data["name"], len(self.sequence)])
            print(f"Received name: {data['name']}")
            client_sock.send((json.dumps({
                "action": "wait"
            }) + "\n").encode())

        # 当人数达到设定人数时，开始游戏
        # self.paler_num决定在有多少人之后开始游戏
        if len(self.clients) == self.player_num:
            print("All clients are ready. Starting the game.")
            print(f"Random number generated: {self.target_number}")
            # 告诉每个人游戏开始
            for client in self.clients:
                client[0].send((json.dumps({
                    "action": "start game"
                }) + "\n").encode())
            # 按照顺序通知当前的人回答猜测
            self.prompt_next_guesser()

    # 准备让下一个人回答
    # 第一轮要按照client注入的顺序
    def prompt_next_guesser(self):
        # 按照记录顺序的表的顺序来进行
        current_client = self.sequence[self.current_guesser]  # ["name", difference]
        current_client_name = current_client[0]
        print(f"Prompting {current_client_name} to guess.")

        # 在clients中找和当前猜测者名字相同的tcp信道，让这个人开始发信
        for client in self.clients:
            if current_client[0] == client[2]:
                client[0].send((json.dumps({
                    "action": "start guess"
                }) + "\n").encode())

    # 判断传入的数字
    def judge_number(self, data, client_sock):
        guess = int(data["number"])
        # 获取当前发猜测数字的人的名字
        current_client_name = self.sequence[self.current_guesser][0]
        print(f"Received guess {guess} from {current_client_name}.", end=" ")

        # 存储与结果的差值
        gap = abs(self.target_number - guess)
        # 更新当前顺序表中每个名字所在的tuple中的数字，代表差值，稍后用作排序
        for c in self.sequence:
            if c[0] == current_client_name:
                c[1] = gap

        # 判断当前猜测是否正确
        # 如果传入猜测与结果相等，代表正确
        if guess == self.target_number:
            message = f"{current_client_name} wins!"
            print(message)
            self.game_over = True
            # 向所有玩家发送游戏结束信息
            for client in self.clients:
                client[0].send((json.dumps({
                    "action": "end",
                    "winner": current_client_name,
                    "number": self.target_number
                }) + "\n").encode())
            time.sleep(1)
            for client in self.clients:
                client[0].close()
            self.sock.close()
        elif guess < self.target_number:  # 小于
            message = "The guess is too low."
            print("Too low.")
            self.broadcast_guess_result(message, guess)
        elif guess > self.target_number:  # 大于
            message = "The guess is too high."
            print("Too high.")
            self.broadcast_guess_result(message, guess)

    # 对所有的玩家发送上一个玩家的猜测结果
    # 让下一个参与者回答
    def broadcast_guess_result(self, message, guess):
        # 从顺序表中获取当前猜测者的名字, 则向他说你猜错了，然后告诉他猜测的结果是大是小
        current_client_name = self.sequence[self.current_guesser][0]
        for client in self.clients:
            client[0].send((json.dumps({
                "action": "wait for turn",
                "name": current_client_name,
                "message": f"{current_client_name} guessed {guess}. {message}"
            }) + "\n").encode())

        # 判断当前轮次是否结束，比对当前current_guesser数字是不是等于len(clients)-1
        if self.current_guesser == len(self.clients) - 1:  # 所有玩家都已猜测
            # 排序difference数组，按第二个元素从大到小排序
            self.sequence = sorted(self.sequence, key=lambda x: x[1], reverse=True)
            # 然后更新self.current_guesser为0，继续沿用新的self.sequence表中的顺序来进行询问
            self.current_guesser = 0

        else:
            # 如果没有结束，就按照顺序表中的下一个
            # self.current_guesser = (self.current_guesser + 1) % len(self.clients)
            self.current_guesser += 1
        self.prompt_next_guesser()

    # 关闭
    def shutdown_server(self):
        print("Shutting down the server.")
        for client in self.clients:
            client[0].close()
        self.sock.close()

    def start(self):
        print(f'Server started on {self.host}:{self.port}')
        try:
            while not self.game_over:
                client_sock, client_address = self.sock.accept()
                threading.Thread(target=self.handle_client, args=(client_sock, client_address)).start()
        except Exception as e:
            pass
        finally:
            self.shutdown_server()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is description!")
    parser.add_argument('--ip', action='store', required=True, dest='ip', help='The IP of server')
    parser.add_argument('--port', action='store', required=True, dest='port', help='The port of server')
    args = parser.parse_args()

    game = Server(args.ip, int(args.port))
    game.start()
