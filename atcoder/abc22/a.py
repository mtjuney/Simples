# coding: utf-8

(n, s, t) = map(int, input().split())
w = int(input())
count = 0
if s <= w and w <= t:
    count += 1

for x in range(n - 1):
    updown = int(input())
    w += updown
    if s <= w and w <= t:
        count += 1

print(count)
