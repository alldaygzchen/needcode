from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_k = 1
        max_k = max(piles)
        res = float('inf')

        while min_k<=max_k:
            
            mid_k = (min_k+max_k)//2
            mid_k_total_hour = 0

            for pile in piles:
                mid_k_total_hour += math.ceil(pile/mid_k)

            if h>=mid_k_total_hour:
                # eat too much
                res = min(res,mid_k)
                max_k = mid_k-1
            else:
                # eat too less
                min_k = mid_k+1

        return res