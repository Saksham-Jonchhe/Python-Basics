class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    list.append(i)
                    list.append(j)
        print(list)
                    
r=Solution()
r.twoSum([1,2,3,4],3)