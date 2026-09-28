def solve(N, A):
    if any(x > 0 for x in A):
        return -1
    return sum(abs(x) for x in A)
data = list(map(int, input().split()))
T = data[0]
pos = 1
for _ in range(T):
    N = data[pos]
    pos += 1
    A = data[pos:pos + N]
    pos += N
    print(solve(N, A))