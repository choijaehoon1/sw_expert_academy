from itertools import product
import copy

def find(j):
    for i in range(H):
        if new_board[i][j] != 0:
            bomb(i,j)
            break

def bomb(x,y):
    size = new_board[x][y]
    new_board[x][y] = 0

    for i in range(1,size):
        for k in range(4):
            nx = x+ i*dx[k]
            ny = y+ i*dy[k]
            if 0<=nx<H and 0<=ny<W and new_board[nx][ny] != 0:
                bomb(nx,ny)
    

def gravity():
    for j in range(W):
        i = H-1
        while i>=0 and new_board[i][j] != 0:
            i -=1

        save = i
        i -= 1

        while i >= 0:
            if new_board[i][j] != 0:
                new_board[save][j] = new_board[i][j]
                save -=1
                new_board[i][j] = 0
            i -= 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for test_case in range(1, T + 1):
    N,W,H = map(int,input().rstrip().split())
    board = []

    for i in range(H):
        board.append(list(map(int,input().split())))


    check = [i for i in range(W)]
    tmp_list = list(product(check,repeat=N))
    # print(tmp_list)

    answer = int(1e9)
    for tmp in tmp_list:
        new_board = copy.deepcopy(board)
        for j in tmp:
            find(j)
            gravity()

        cnt = 0
        for i in range(H):
            for j in range(W):
                if new_board[i][j] != 0:
                    cnt += 1
        answer = min(answer,cnt)      

    print('#'+str(test_case), answer)

