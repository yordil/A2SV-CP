class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = num1
        a+="*"
        a+=num2
        return str(eval(a))