n = 1270
count = 0

list = [500, 100, 20, 10]

for i in list:
    count += n // i
    n = n % i

print(count)
