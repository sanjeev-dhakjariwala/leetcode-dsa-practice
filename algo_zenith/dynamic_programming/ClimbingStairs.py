import sys

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    result = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        result.append(str(n // m + n % m))
        index += 2
    sys.stdout.write("\n".join(result) + "\n")

if __name__ == "__main__":
    main()
