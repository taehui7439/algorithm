nlocation = input()

row = int(nlocation[1])
col = int(ord(nlocation[0]) - ord('a') + 1)

nrow, ncol = 0, 0
count = 0

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (-1, 2), (1, -2), (-1, -2)]

for step in (steps):
    nrow = row + step[0]
    ncol = col + step[1]

    if(nrow >= 1 and nrow <= 8 and ncol >= 1 and nrow <= 8):
        count += 1

print(count)
