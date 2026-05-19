class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums2)
        ans = float('inf')
        for i in range(len(nums1)):
            if nums1[i] in s:
                ans = min(ans,nums1[i])

        return -1 if ans == float('inf') else ans