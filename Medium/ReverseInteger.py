class Solution:
    def reverse(self, x: int) -> int:
        d = 0
        rev = 0
        if x<0:
            x=x*(-1)
            while(x>0):
                d = x%10
                x = x//10
                rev = (rev*10)+d
            rev = rev*(-1)
        else:     
            while(x>0):
                d = x%10
                x = x//10
                rev = (rev*10)+d
        if rev<((-2)**31) or rev>((2**31)-1):
            return 0
        else:
            return rev
