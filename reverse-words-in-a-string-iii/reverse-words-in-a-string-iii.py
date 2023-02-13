class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res=[]
        for i in words:
            a = list(i)
            res.append("".join(a[::-1]))
        
        return " ".join(res)
    
    