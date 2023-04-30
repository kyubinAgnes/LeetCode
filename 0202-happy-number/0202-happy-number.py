class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while True:
            ret = 0
            for x in str(n):
                visited.add(int(x))
                ret += int(x) * int(x)
                
            if ret == 1:
                return True
            
            if ret in visited:
                return False
            n = ret