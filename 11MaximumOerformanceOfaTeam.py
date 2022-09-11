# Question: https://leetcode.com/problems/maximum-performance-of-a-team/

# Solution:
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engg = []
        for eff, spd in zip(efficiency, speed):
            engg.append([eff, spd])
        engg.sort(reverse=True)
        
        prfm, speed = 0, 0
        heap = []
        
        for eff, spd in engg:
            if len(heap) == k:
                speed -= heapq.heappop(heap)
            speed += spd
            heapq.heappush(heap, spd)
            prfm = max(prfm, eff * speed)
        
        return prfm
      
# Verdict:
# Runtime: 1511 ms, faster than 5.07% of Python3 online submissions for Maximum Performance of a Team.
# Memory Usage: 31.2 MB, less than 37.55% of Python3 online submissions for Maximum Performance of a Team.
