
# key_list = list(b.keys())

# print(key_list)

# 그리디 0번

# n=1260
# count=0

# array=[500,100,50,10]

# for coin in array:
#   count += n // coin
#   n %= coin

# print(count)



# 그리디 1번

# count = 0
# n,m = map(int,input().split())

# while True:
#   target = (n // m) * m
#   count += (n-target)
#   n = target

#   if n < m:
#     break

#   count += 1
#   n //= m

# count += (n-1)
# print(count)



# 그리디 2번

# s = input()
# n = int(s[0])

# for i in range(1,len(s)):
#   m = int(s[i])
#   if m <= 1 or n <= 1:
#     n += m
#   else:
#     n *= m

# print(n)



# 그리디 3번

# n = int(input())
# m = list(map(int,input().split()))
# m.sort()
#
# group = 0
# count = 0
#
# for i in m:
#   count += 1
#
#   if count > i:
#     group += 1
#     count = 0
#
# group += 1
#
# print(group)



# 백준 11047번

# n, k = (input().split())
# n = int(n)
# k = int(k)
# count = 0
# a=[]
# for i in range(0,n):
#   a.append(int(input()))
#
# a.reverse()
#
# for i in range(n):
#
#   while k !=0:
#     count += k // a[i]
#     k %= a[i]
#     i += 1
#
# print(count)



# 11399번

# n = (input())
# m = list(map(int,input().split()))
# m.sort()
#
# i=0
# result = 0
# count = int(n)
#
# for i in range(1,count):
#   m[i] += m[i-1]
#
# print(sum(m))
