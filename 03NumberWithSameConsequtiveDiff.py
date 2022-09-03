# Question: https://leetcode.com/problems/numbers-with-same-consecutive-differences/

# Solution:
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        queue = [digit for digit in range(1, 10)]
        
        for level in range(n-1):
            nxt_queue = []
            for num in queue:
                tail = num % 10
                nextDigits = set([tail+k, tail-k])
                
                for nextDigit in nextDigits:
                    if 0 <= nextDigit < 10:
                        newNum = num * 10 + nextDigit
                        nxt_queue.append(newNum)
                queue = nxt_queue
        return queue
      
# Verdict:
# Runtime: 70 ms, faster than 43.88% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.3 MB, less than 41.16% of Python3 online submissions for Numbers With Same Consecutive Differences.
