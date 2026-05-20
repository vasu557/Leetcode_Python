class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        temp1 = set()
        temp2 = set()
        ans = []
        for i in range(len(A)):
            temp1.add(A[i])
            temp2.add(B[i])
            temp = temp1 & temp2
            ans.append(len(temp))

        return ans