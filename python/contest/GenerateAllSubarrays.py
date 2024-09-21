class Solution:
    def generate_all_subarrays(self, arr):
        subarrays = []

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray = arr[i:j + 1]
                subarrays.append(subarray)

        return subarrays


sol = Solution()
print(sol.generate_all_subarrays([1, 2, 3]))
