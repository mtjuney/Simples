N = int(input())

SS = []
for i in range(N):
    SS.append(map(int, input().split()))

blacked = []

for S_inc, C in SS:

    S = S_inc - 1

    del_black_indexes = []
    black_i = -1
    S0 = None
    for i in range(len(blacked)):
        h0, h1 = blacked[i]
        if h0 <= S and h1 >= S:
            if not S0:
                S0 = h0
            S = h1 + 1
            black_i = i
            del_black_indexes.append(i)
        elif S > h1:
            black_i = i


    if not S0:
        S0 = S

    add_count = 0

    for i in range(black_i + 1, len(blacked)):
        h0, h1 = blacked[i]
        if S + add_count + C - 1 >= h0:
            add_count += h1 - h0 + 1
            del_black_indexes.append(i)
        else:
            break

    S = S + add_count + C - 1

    print(S + 1)
    for del_black_index in sorted(del_black_indexes, reverse=True):
        del blacked[del_black_index]
    blacked.append((S0, S))
    blacked = sorted(blacked, key=lambda x:x[0])
