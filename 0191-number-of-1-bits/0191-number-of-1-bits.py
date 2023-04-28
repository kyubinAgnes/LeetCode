class Solution:
    def hammingWeight(self, n: int) -> int:
        str_n = str(bin(n))
        cnt = Counter(str_n)
        
        if '1' in list(cnt.keys()):
            answer = cnt['1']
        else:
            answer = 0
        
        return answer