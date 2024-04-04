from typing import List
class Solution:
    def minimumTime(self, power: List[int]) -> int:
        power.sort(reverse=True)
        print(power)
        return self.helper(0, power)

    def helper(self,curr_index, power):
        if curr_index == len(power)-1:
            return power[curr_index]

        min_val = 2147483647

        for i in range(curr_index,len(power)-1):
            self.swap(power, curr_index,i)
            prev_min_val = self.helper(curr_index+1, power)
            gain = len(power) - curr_index
            curr_val = int(power[curr_index] / gain)
            curr_val += prev_min_val
            if power[curr_index] % gain != 0:
                curr_val += 1
            min_val = min(min_val, curr_val)
            self.swap(power, curr_index,i)

        return min_val

    def swap(self, power, index1, index2):
        temp_val = power[index1]
        power[index1]= power[index2]
        power[index2]=temp_val
        return


if __name__ == '__main__':
    obj = Solution()
    print(obj.minimumTime([1,2,9,4]))