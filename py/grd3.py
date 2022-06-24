n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
result = 0
print(first, second)

count = int(m / (k+1)) * k
count2 = m - count

result += count * first
result += count2 * second

print(result)
