#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())

def combi():
    tmp = ''
    cnt = 0
    for i in range(N):
        cnt += 1
        tmp += q[i]
		        
        if cnt == length:
            if tmp not in answer:
            	answer.append(tmp)
            cnt = 0
            tmp = ''

def change(tmp):
    cnt = 0
    num = 0
    for i in range(len(tmp)-1,-1,-1):
        if tmp[i].isnumeric():
            num += int(tmp[i]) * (16**cnt)
        else:
            if tmp[i] == 'A':
                num += 10 * (16**cnt)
            if tmp[i] == 'B':
                num += 11 * (16**cnt)                
            if tmp[i] == 'C':
                num += 12 * (16**cnt)                
            if tmp[i] == 'D':
                num += 13 * (16**cnt)                
            if tmp[i] == 'E':
                num += 14 * (16**cnt)                
            if tmp[i] == 'F':
                num += 15 * (16**cnt)                                
        cnt += 1                
    
    return num
        
    

for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    data = list(input())
    q = deque()
    length = N//4
    answer = []
    for i in data:
        q.append(i)
    
    combi()
    
    for i in range(length-1):
        q.rotate(1)        
        combi()
    
    idx = 0
    for i in answer:
        num = change(i)
        answer[idx] = num
        idx += 1
    
    answer.sort(reverse = True)
    print('#'+str(test_case), answer[K-1])
    
