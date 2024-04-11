from collections import deque, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freq_count = defaultdict(int)
        start_index =-1
        min_index = ""
        for ch in t:
            freq_count[ch]+=1
        #print(freq_count)
        for i in range(len(s)):
            if s[i] in freq_count:
                if start_index==-1:
                    start_index=i
                freq_count[s[i]]-=1

                while (freq_count[s[i]]<0  and s[start_index] == s[i]) or s[start_index] not in freq_count:
                    if s[start_index] in freq_count:
                        freq_count[s[start_index]]+=1
                    start_index+=1

                if all(value <= 0 for value in freq_count.values()):
                    if len(min_index) == 0 or len(min_index)>(i-start_index+1):
                        min_index = s[start_index: i+1]
                    # remove a character till the condition becomes invalid
                    freq_count[s[start_index]]+=1
                    start_index+=1
                    while start_index < len(s) and (s[start_index] not in freq_count or freq_count[s[start_index]]<0):
                        if s[start_index] in freq_count:
                            freq_count[s[start_index]]+=1
                        start_index+=1

        return min_index


if __name__ == '__main__':
    sol_obj = Solution()
    print(sol_obj.minWindow("aaaaaaaaaaaabbbbbcdd","abcdd")=="abbbbbcdd")
    print(sol_obj.minWindow("acbbaca", "aba")=="baca" )