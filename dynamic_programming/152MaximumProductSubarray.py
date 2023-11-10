class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = max_product

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result


# Example 1
nums1 = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProduct(nums1))  # Output: 6

# Example 2
nums2 = [-2, 0, -1]
print(sol.maxProduct(nums2))  # Output: 0
