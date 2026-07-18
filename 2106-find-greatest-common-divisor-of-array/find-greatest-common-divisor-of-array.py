class Solution:

    def myFunction(self,a, b):
        while a != 0 and b != 0 :
            if a >= b:
                a = a -b
            elif b > a:
                b = b- a
        
        if a == 0:
            return b
        if b == 0:
            return a

    def findGCD(self, nums: List[int]) -> int:
        mini = float('inf')
        maxi = float('-inf')
        for x in range(0,len(nums)):
            if nums[x] <= mini :
                mini = nums[x]
            if nums[x] >= maxi:
                maxi = nums[x]

        return  self.myFunction(mini,maxi)
        