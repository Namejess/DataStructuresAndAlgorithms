class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        res = ''

        for i in strs:
            for j in range(strs[i]):
                print(j)