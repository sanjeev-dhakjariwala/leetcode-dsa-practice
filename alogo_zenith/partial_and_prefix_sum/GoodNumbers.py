
# Write your code here

# you can set your Template at profile settings [https://maang.in/profile/template-code]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    q = int(data[index])
    index += 1

    N = 1000005
    arr = [0] * N

    for _ in range(n):
        l = int(data[index])
        index += 1
        r = int(data[index])
        index += 1
        arr[l] += 1
        arr[r + 1] -= 1

    for i in range(1, N):
        arr[i] += arr[i - 1]

    for i in range(1, N):
        arr[i] = 1 if arr[i] >= k else 0

    prefixSum = [0] * N
    for i in range(1, N):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    results = []
    for _ in range(q):
        l = int(data[index])
        index += 1
        r = int(data[index])
        index += 1
        ans = prefixSum[r] - prefixSum[l - 1]
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()