from typing import List
class Solution:
    def minimumTime(self, power: List[int]) -> int:
        power.sort(reverse=True)
        mem = [ [-1]*(1<<len(power)) for i in range(len(power))]
        return self.helper(0, power,0,mem)

    def helper(self,curr_index, power,mask,mem):
        if curr_index == len(power):
            # temp_mask = mask^7
            # print(mask)
            # print(temp_mask)
            return 0
        if mem[curr_index][mask]!=-1:
            return mem[curr_index][mask]

        min_val = 2147483647
        for i in range(len(power)):
            if mask&(1<<i) == 0:
                prev_min_val = self.helper(curr_index+1, power, mask|(1<<i),mem)
                gain = len(power) - curr_index
                curr_val = int(power[i] / gain)
                curr_val += prev_min_val
                if power[i] % gain != 0:
                    curr_val += 1
                min_val = min(min_val, curr_val)
        mem[curr_index][mask]=min_val
        return mem[curr_index][mask]