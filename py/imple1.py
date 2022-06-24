a = int(input())

direction = (input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0, ]
dir = ['L', 'R', 'U', 'D']

x = 1
y = 1

for d in direction:
    for i in range(len(dir)):
        if d == dir[i]:
            nx = x+dx[i]
            ny = y+dy[i]

    if nx < 1 or ny < 1 or nx > a or ny > a:
        continue

    x, y = nx, ny

print(x, y)
