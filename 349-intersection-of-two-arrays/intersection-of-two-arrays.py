class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = list(set(nums1) & set(nums2))
        temp.sort(reverse = True)

        return temp
