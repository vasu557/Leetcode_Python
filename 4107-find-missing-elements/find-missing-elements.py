class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        st = set()
        mini = float('inf')
        maxi = float('-inf')
        for i in range(0,len(nums)):
            st.add(nums[i])
            if nums[i] < mini:
                mini = nums[i]
            if nums[i] > maxi:
                maxi = nums[i]

        for i in range(mini,maxi + 1):
            if i not in st:
                res.append(i)

        
        return res


                