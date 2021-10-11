class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return n
        
        ret1 =1
        ret2 =2
        current=0
        for i in range(2,n):
            current = ret1 + ret2
            ret1 =  ret2
            ret2 = current
        return current
         