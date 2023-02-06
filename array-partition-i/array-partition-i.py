class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()
        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum