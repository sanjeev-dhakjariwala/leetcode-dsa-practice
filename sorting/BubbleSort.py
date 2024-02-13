class Sort:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n - 1):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


sor = Sort()
arr = [4, 1, 3, 9, -7]
sor.bubbleSort(arr)
print(arr)