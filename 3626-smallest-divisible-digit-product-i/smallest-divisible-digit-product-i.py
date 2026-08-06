class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        temp = n
        ans = -1
        while True:
            temp2 = str(temp)
            prod = 1
            for i in range(0,len(temp2)):
                prod *= int(temp2[i])
            
            if prod % t == 0:
                ans = temp
                break
            
            temp += 1
        
        return ans

            


        