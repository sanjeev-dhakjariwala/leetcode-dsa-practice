class Solution:
    def merge(self, arr, l, m, r):
        # code here
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        # code here
        if l < r:
            m = (l + (r - 1)) // 2

            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)


sol = Solution()
arr = [4, 1, 3, 9, 7]
sol.mergeSort(arr, 0, len(arr) - 1)
print(arr)
