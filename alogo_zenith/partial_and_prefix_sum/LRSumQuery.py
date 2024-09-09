# Write your code here

# you can set your Template at profile settings [https://maang.in/profile/edit-profile]

N, Q = map(int, input().split())

A = list(map(int, input().split()))

queries = []

for _ in range(Q):
    L, R = map(int, input().split())
    queries.append((L, R))
""" N = 10
Q = 10
A = [12, -23, -123, 2345, 2345, 44, 345, -93945, -5353, 1] """
prefix_sum = [0] * (N + 1)
queries = [
    (1, 5),
    (1, 8),
    (1, 10),
    (2, 2),
    (6, 6),
    (4, 8),
    (2, 9),
    (4, 10),
    (3, 6),
    (5, 9),
]
for i in range(N):
    prefix_sum[i + 1] = (prefix_sum[i] + A[i]) % ((10 ** 9) + 7)

for L, R in queries:
    ans = prefix_sum[(R-1) + 1] - prefix_sum[(L - 1)]
    print(ans)
