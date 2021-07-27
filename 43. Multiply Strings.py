class Solution:
    def multiply(self, num1, num2):
        res = 0
        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res += (ord(n1) - ord('0')) * (ord(n2) - ord('0')) * (10**(i+j))
        return str(res)