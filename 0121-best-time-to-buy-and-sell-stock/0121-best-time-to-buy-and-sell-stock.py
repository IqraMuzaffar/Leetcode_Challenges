class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        max=0
        while(r<len(prices)):
            if(prices[r]>prices[l]):
                if(prices[r]-prices[l])>max:
                    max=prices[r]-prices[l]
            else:
                l=r
            r+=1
        return max