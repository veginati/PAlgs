class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set({})
        start_index=0
        long_sub_str=""
        i =0
        while i<len(s):
            if s[i] not in unique:
                unique.add(s[i])
            else:
                if len(long_sub_str)<(i-start_index+1):
                    long_sub_str= s[start_index:i]
                while s[i] in unique:
                    unique.remove(s[start_index])
                    start_index+=1
                unique.add(s[i])
            i+=1
        if len(long_sub_str)<(i-start_index+1):
            long_sub_str= s[start_index:i]

        return len(long_sub_str)

if __name__ == '__main__':
    sol_obj = Solution()
    print(sol_obj.lengthOfLongestSubstring(" abcdefghaswerdhtreeh"))