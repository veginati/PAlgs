class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set({})
        start_index=0
        long_sub_str=""

        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
            elif len(long_sub_str) ==0 or len(long_sub_str)<(i-start_index+1):
                long_sub_str= s[start_index:i]

                while s[i] in unique:
                    unique.remove(s[start_index])
                    start_index+=1
                unique.add(s[i])
        print(long_sub_str)
        return len(long_sub_str)


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring("bbbb"))