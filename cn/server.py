
from socket import *
from time import ctime, sleep

heaps = [7, 5, 3]
ending = [0, 0, 0]
last_played_by = 0
moves_cnt = 0

BUFSIZ = 1024

def Alice_init():
    HOST = ''
    PORT = 20009
    ADDR = (HOST, PORT)
    tcpSerSockAlice = socket(AF_INET, SOCK_STREAM)
    tcpSerSockAlice.bind(ADDR)
    tcpSerSockAlice.listen(5)
    tcpCliSockAlice, addr = tcpSerSockAlice.accept()
    return tcpCliSockAlice


def Bob_init():
    HOST = ''
    PORT = 30009
    ADDR = (HOST, PORT)
    tcpSerSockBob = socket(AF_INET, SOCK_STREAM)
    tcpSerSockBob.bind(ADDR)
    tcpSerSockBob.listen(5)
    tcpCliSockBob, addr = tcpSerSockBob.accept()
    return tcpCliSockBob


def declare_winner(tcpCliSockCurr, tcpCliSockNxt):
    if last_played_by == 1:
        data = "-1 Alice"
    else:
        data = "-1 Bob"
    tcpCliSockCurr.send(bytes(data, 'utf-8'))
    tcpCliSockNxt.send(bytes(data, 'utf-8'))


def Player_play(tcpCliSockCurr, tcpCliSockNxt):
    global moves_cnt
    #sleep(3)
    data = tcpCliSockCurr.recv(BUFSIZ) # RECEIVE DATA FROM CURRENT PLAYER
    print(data.decode('utf-8'))
    #sleep(3)
    tcpCliSockNxt.send(data)   # SEND DATA TO NEXT PLAYER

    moves = data.decode('utf-8').split()

    if heaps == ending:
        declare_winner(tcpCliSockCurr, tcpCliSockNxt)

    qt = len(moves)# - moves_cnt
    pile = moves[-1][0]
    if pile == 'A':
        pl = 0
    elif pile == 'B':
        pl = 1
    else:
        pl = 2
    #moves_cnt = len(moves)
    print(pl, qt)
    return pl, qt


if __name__ == '__main__':
    #heaps, ending, last_played_by
    AliceSoc = Alice_init()
    BobSoc = Bob_init()
    print("State : ", heaps)
    while (heaps != ending):

        last_played_by = not last_played_by
        if last_played_by == 1:
            pl, qt = Player_play(AliceSoc, BobSoc)
        else:
            pl, qt = Player_play(BobSoc, AliceSoc)

        if qt <= heaps[pl]:
            heaps[pl] -= qt
        else:
            heaps[pl] = 0
        print("State : ", heaps)

    print("Winner : ", last_played_by)
