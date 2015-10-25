N, M = map(int, input().split())
A = map(int, input().split())
B = map(int, input().split())

if N < M:
    print('NO')
    exit()

A_s = sorted(A, reverse=True)
B_s = sorted(B, reverse=True)

fail_room = 0
flag = True
for i, b in enumerate(B_s):
    if b > A_s[i]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
