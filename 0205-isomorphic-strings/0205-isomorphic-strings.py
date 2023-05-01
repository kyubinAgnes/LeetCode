class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for idx in range(len(s)):
            char1, char2 = s[idx], t[idx]
            if char1 not in d:
                if char2 in d.values():
                    return False
                d[char1] = char2
            elif d[char1] != char2:
                return False
        return True