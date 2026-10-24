class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens.pop())
        
        nums = []
        ops = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in ops:
                nums.append(t)
            if t in ops:
                if t == "+":
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(x + y)
                elif t == "*":   
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(x * y)
                elif t == "-":   
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(y - x)
                elif t == "/":  
                    x = int(nums.pop())
                    y = int(nums.pop())
                    nums.append(int(y / x))
        return nums.pop()