class Solution:
    def calculate(self, s: str) -> int:
        def apply_operator(operand_stack, operator_stack):
            if not operator_stack:
                return
            operator = operator_stack.pop()
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            if operator == "+":
                operand_stack.append(left_operand + right_operand)
            elif operator == "-":
                operand_stack.append(left_operand - right_operand)
            elif operator == "*":
                operand_stack.append(left_operand * right_operand)
            elif operator == "/":
                operand_stack.append(int(left_operand / right_operand))

        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        operand_stack = []
        operator_stack = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                operand_stack.append(int(s[i:j]))
                i = j
            elif s[i] in precedence:
                while (
                    operator_stack
                    and precedence[operator_stack[-1]] >= precedence[s[i]]
                ):
                    apply_operator(operand_stack, operator_stack)
                operator_stack.append(s[i])
                i += 1
            else:
                apply_operator(operand_stack, operator_stack)
                i += 1
        while operator_stack:
            apply_operator(operand_stack, operator_stack)
        return operand_stack[-1]


sol = Solution()
print(sol.calculate(" 3+5 / 2 "))