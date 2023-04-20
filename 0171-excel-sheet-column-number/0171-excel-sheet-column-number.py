class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        
        i = 1
        for letter in columnTitle[::-1]:
            number_represented = ord(letter) - 64
            number_to_add = number_represented * (26**(i-1))
            column_number += number_to_add
            i += 1
        
        return column_number