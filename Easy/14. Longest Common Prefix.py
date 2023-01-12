class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        s = min(strs, key=len)
        for i in s:
            flag = 0
            for j in strs:
                if j[len(res)] != i:
                    flag = 1
                    break
            if flag == 0:
                res += i
        return res