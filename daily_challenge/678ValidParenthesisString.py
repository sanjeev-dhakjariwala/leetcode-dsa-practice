class Solution:
    def checkValidString(self, s: str) -> bool:
        # Stacks to keep track of indices of '(' and '*' characters
        left_stack = []
        star_stack = []

        # Iterate through the string
        for i, char in enumerate(s):
            if char == "(":
                left_stack.append(i)
            elif char == "*":
                star_stack.append(i)
            elif char == ")":
                # If there are '(' in the left_stack, pop one '('
                if left_stack:
                    left_stack.pop()
                # If there are '*' in the star_stack, pop one '*'
                elif star_stack:
                    star_stack.pop()
                else:
                    # If no '(' or '*' to match ')', return False
                    return False

        # Match remaining '(' and '*' if any
        while left_stack and star_stack:
            # If '*' comes after '('
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                # '*' comes before '('
                break

        # If after the matching process, left_stack is empty, then it's valid
        return not left_stack


sol = Solution()
print(sol.checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()"))
