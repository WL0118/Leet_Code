class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        for ele in stones:
            for jewel in jewels:
                if(ele==jewel):
                    count+=1
        return count