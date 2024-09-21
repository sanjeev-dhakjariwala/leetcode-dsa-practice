class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j = len(a) - 1, len(b) - 1
        carry = "0"
        while i > -1 or j > -1:
            t1 = a[i] if i > -1 else "0"
            t2 = b[j] if j > -1 else "0"

            if t1 == "1" and t2 == "1":
                if carry == "0":
                    sum_binary = "0"
                else:
                    sum_binary = "1"
                carry = "1"
                res = sum_binary + res
            else:
                sum_binary = str(int(t1) + int(t2))
                if sum_binary == "1" and carry == "1":
                    carry = "1"
                    res += "0"
                else:
                    res = str(int(sum_binary) + int(carry)) + res
                    carry = "0"

            i -= 1
            j -= 1

        if carry == "1":
            res = carry + res

        return res


sol = Solution()
print(sol.addBinary("1111", "1111"))
