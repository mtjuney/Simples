N, M = map(int, input().split())

A = map(int, input().split())

ans = [0] * (M + 1)

for a in A:
    ans[a] += 1

i, maxi = sorted(enumerate(ans), key=lambda x:x[1], reverse=True)[0]

if maxi > N // 2:
    print(i)
else:
    print('?')
