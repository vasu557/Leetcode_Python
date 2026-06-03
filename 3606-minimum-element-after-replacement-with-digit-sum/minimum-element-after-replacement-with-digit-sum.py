class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = []
        for sum in nums:
            temp = 0
            while sum > 0:
                rem = sum % 10
                temp += rem
                sum //= 10

            res.append(temp)
        
        return min(res)