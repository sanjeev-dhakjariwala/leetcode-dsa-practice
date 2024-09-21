class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Base case for multiplying by 0
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Result array to store the product of each digit multiplication
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both strings to simplify position management
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit and add to the result array
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit_mul = int(num1[i]) * int(num2[j])
                result[i + j] += digit_mul
                result[i + j + 1] += result[i + j] // 10  # Carry to the next position
                result[i + j] %= 10  # Keep only the last digit in the current position
        
        # Remove leading zeros and convert to string
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Join the result digits to form the final product string
        return ''.join(map(str, result[::-1]))


sol = Solution()
num1 = "123"
num2 = "456"
print(sol.multiply(num1, num2))