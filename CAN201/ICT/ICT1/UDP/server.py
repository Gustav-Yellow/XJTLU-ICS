# Server side
import argparse
import json
import random
from socket import *


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        # 创建UDP连接
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(('', port))
        # 生成的随机数
        self.target_number = None
        # 保存client信息
        self.clients = []  # [client_address, client_name]
        self.current_guesser = 1

    # 用户进入
    def participant_action(self, data: json, client_address):
        # 如果此时client传回的信息中没有名字，代表是刚建立连接，这个时候需要server发送信息询问client的用户名
        if data['name'] is None:
            # 展示连接信息
            print("Client connected: " + client_address[0] + ":" + str(client_address[1]))
            self.sock.sendto(json.dumps({
                "action": "ask name",
            }).encode(), client_address)
        elif data['name'] is not None:  # 其他情况下就是当做接收的名字，保存用户信息
            self.clients.append((client_address, data["name"]))
            # 展示当前接收到的用户名
            print("Received name: " + data["name"])
            # 通知客户端需要等待另一名用户的加入
            self.sock.sendto(json.dumps({
                "action": "wait"
            }).encode(), client_address)

        # 人数到两人之后开始游戏
        if len(self.clients) == 2:
            print("All clients are ready. Starting the game.")
            print("Random number generated: " + str(self.target_number))
            # 通知游戏即将开始
            for c in self.clients:
                self.sock.sendto(json.dumps({
                    "action": "start game"
                }).encode(), (c[0][0], c[0][1]))
            self.switch_turn(data, message=None)

    # 切换角色顺序
    def switch_turn(self, data, message):
        wrong_guesser = self.current_guesser
        self.current_guesser = 1 if self.current_guesser == 0 else 0
        if "number" not in data:
            # 证明这个是第一个判断
            self.sock.sendto(json.dumps({
                "action": "start guess"
            }).encode(), self.clients[self.current_guesser][0])
            # 告诉另一个客户端先等待
            self.sock.sendto(json.dumps({
                "action": "wait for turn"
            }).encode(), self.clients[wrong_guesser][0])
        else:
            # 给发送错误的人
            self.sock.sendto(json.dumps({
                "action": "wrong",
                "message": message
            }).encode(), self.clients[wrong_guesser][0])
            # 发给下一个人
            self.sock.sendto(json.dumps({
                "action": "your turn",
                "message": self.clients[wrong_guesser][1] + " guessed " + str(data["number"]) + ". " + message
            }).encode(), self.clients[self.current_guesser][0])

    # 进行游戏
    def judge_number(self, data: json):
        if int(data["number"]) == self.target_number:
            for c in self.clients:
                self.sock.sendto(json.dumps({
                    "action": "end",
                    "winner": self.clients[self.current_guesser][1],
                    "number": self.target_number
                }).encode(), (c[0][0], c[0][1]))
        elif data["number"] < self.target_number:
            notice = "The guess is too low."
            self.switch_turn(data, notice)
        elif data["number"] > self.target_number:
            notice = "The guess is too high."
            self.switch_turn(data, notice)

    # 游戏开始
    def start(self):
        self.target_number = random.randint(1, 100)
        print('Server started on ' + self.host)

        while True:
            try:
                # 接收到的client_address中的信息格式是元组[ip, port]
                data, client_address = self.sock.recvfrom(20480)
                data = json.loads(data)

                # 判断当前客户端想要进行的操作
                if data["action"] == 'participate':  # 如果当前是用client希望加入或者提交名字
                    self.participant_action(data, client_address)
                elif data["action"] == 'game':  # 如果当前是client发送的数字猜测
                    self.judge_number(data)
            except Exception as e:
                print("Error message: " + str(e))


# 运行主程序
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is description!")
    parser.add_argument('--ip', action='store', required=True, dest='ip', help='The IP of server')
    parser.add_argument('--port', action='store', required=True, dest='port', help='The port of server')
    args = parser.parse_args()

    # 游戏启动
    game = Server(args.ip, int(args.port))
    game.start()
