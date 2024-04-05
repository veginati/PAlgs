# printing all subsets using bit-masking
from typing import List
class GenerateSets(object):

    # generate combination sets using bit masking
    # Time complexity is O( power(2,n) * n)
    # Space : O( power(2,n))
    def generate(self, numbers: List[int]):
        total_subsets =[]
        count = 1<<len(numbers) # total subsets = power(2,n)
        print(count)
        for i in range(count):
            temp_set=[]
            for j in range(len(numbers)):
                if i & (1<<j) !=0:
                    temp_set.append(numbers[j])
            total_subsets.append(temp_set)
        return total_subsets



if __name__ == "__main__":
    generate_obj = GenerateSets();
    print(generate_obj.generate([1,2,3]))
