from functools import wraps
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

serversocket.bind((host, port))
serversocket.listen(2)

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        # print(f'send to({args[1]})' + args[0])
        return func(*args, **kwargs)
    return with_logging

@logit
def send_msg(msg, players:list):
    if type(players) == list:
        for i in players:
            print(f'send to({i})' + msg)
            clientsocket = i['socket']
            clientsocket.send(msg.encode('utf-8'))
    else:
        print(f'send to({players})' + msg)
        clientsocket = players['socket']
        clientsocket.send(msg.encode('utf-8'))


players = []
while True:
    clientsocket, addr = serversocket.accept()
    print(addr, type(addr))
    # send_msg('hello', addr)
    players.append({'player': f'player{len(players)+1}', 
                    'addr': addr,
                    'socket': clientsocket})
    welcome_msg = f"欢迎 {players[-1]['player']} 加入游戏，目前房间人数 {len(players)} 人。"
    # print(welcome_msg)
    send_msg(welcome_msg, players)
    
    if len(players)<2:
        wait_for_player = f'请等待其他玩家加入游戏。'
        send_msg(wait_for_player, players)
        continue
    else:
        start_msg = '玩家人数足够，游戏开始！'
        send_msg(start_msg, players)
        