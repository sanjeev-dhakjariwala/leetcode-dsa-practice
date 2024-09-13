
# Write your code here

# you can set your Template at profile settings [https://maang.in/profile/template-code]
MOD = 1000000007
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    
    n = int(data[index])
    index += 1
    q = int(data[index])
    index += 1

    arr = [0] * (n + 1)
    mulArr = [0] * (n + 1)

    for i in range(1, n + 1):
        arr[i] = int(data[index])
        index += 1
        mulArr[i] = arr[i] * i % MOD

    for i in range(1, n + 1):
        arr[i] = (arr[i] + arr[i - 1]) % MOD
        mulArr[i] = (mulArr[i] + mulArr[i - 1]) % MOD

    results = []
    for _ in range(q):
        l = int(data[index])
        index += 1
        r = int(data[index])
        index += 1
        ans = (mulArr[r] - mulArr[l - 1]) % MOD
        ans = (ans - (l - 1) * (arr[r] - arr[l - 1]) % MOD) % MOD
        ans = (ans + MOD) % MOD
        results.append(ans)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()