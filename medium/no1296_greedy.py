class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        print(nums.sort())



        my_dict = {}
        for ele in nums:
            if(ele in my_dict):
                my_dict[ele]=my_dict[ele]+1
            elif(ele not in my_dict):
                my_dict[ele]=1
        
        while(bool(my_dict)):
            first=list(my_dict.keys())[0]
            for ele in range(first,first+k):
                try:
                    my_dict[ele]=my_dict[ele]-1
                    if(my_dict[ele]==0):
                        del my_dict[ele]
                except:
                    return False

        return True