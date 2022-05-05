class Solution:
    def isPalindrome(self, s: str) -> bool:
        if 1 <= len(s): 
            d = ""
            for i in s:
                if i.isalpha() == True or i.isdigit() == True:
                    d = d+i
            d = d.lower()
            rd = ""
            for i in d:
                rd = i+rd

            if rd==d:
                return True
            else:
                return False
        else:
            return False
