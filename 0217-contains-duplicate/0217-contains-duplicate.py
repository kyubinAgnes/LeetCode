class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)) : 
            temp = dic.get(nums[i],2)
            if temp != 2 :
                return True
            dic[nums[i]] = 1
        return False