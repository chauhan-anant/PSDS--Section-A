#1--------------------------------
n = int(input("Enter N: "))
k = int(input("Enter K: "))
arr = list(map(int, input("Enter array elements: ").split()))
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, n):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    max_sum = max(max_sum, window_sum)
print("Maximum Sum:", max_sum)

#2--------------------------------
s = input("Enter string: ")
left = 0
max_length = 0
characters = set()
for right in range(len(s)):
    while s[right] in characters:
        characters.remove(s[left])
        left += 1
    characters.add(s[right])
    max_length = max(max_length, right - left + 1)
print("Longest Length:", max_length)

#3--------------------------------
n, m, k = map(int, input("Enter N, M and K: ").split())
edges = []
for i in range(m):
    u, v, w = map(int, input("Enter u, v and weight: ").split())
    edges.append((u, v, w))
INF = float('inf')
dp = [INF] * (n + 1)
dp[1] = 0
for _ in range(k):
    new_dp = dp.copy()
    for u, v, w in edges:
        if dp[u] != INF:
            new_dp[v] = min(new_dp[v], dp[u] + w)
        if dp[v] != INF:
            new_dp[u] = min(new_dp[u], dp[v] + w)
    dp = new_dp
if dp[n] == INF:
    print("-1")
else:
    print("Minimum Path Weight:", dp[n])