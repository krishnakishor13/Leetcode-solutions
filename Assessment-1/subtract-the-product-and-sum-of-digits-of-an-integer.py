
#### Python-3 #####
###################


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = 0
        product = 1

        while(n>0):
            x = n%10
            temp = temp + x
            product = product * x
            n = n//10  
        return product-temp

