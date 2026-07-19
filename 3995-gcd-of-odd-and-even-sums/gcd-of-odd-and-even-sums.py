class Solution:
    def myFunction(self,a,b):
        while a != 0 and b != 0:
            if a >= b:
                a = a-b
            elif b > a:
                b = b -a
        return b if a == 0 else a
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0
        for i in range(1,2*n+1):
            if i % 2 == 0:
                even += i
            else:
                odd += i
        
        return self.myFunction(even,odd)
