class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        flag = 0
        for i in range(0,len(s)):
            if(flag>0):
                flag = 0
                continue
            if(i<len(s)-1 and dic[s[i]]<dic[s[i+1]]):
                sum += dic[s[i+1]]-dic[s[i]]
                flag += 1
                print()
            else:
                sum += dic[s[i]]
            print(sum)
        return sum