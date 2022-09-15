# Queation: https://leetcode.com/problems/find-original-array-from-doubled-array/

# Code:
class Solution:
    def findOriginalArray(self, arr):
        cnt, ans = Counter(arr), []
        for num in sorted(arr, key = lambda x: abs(x)):
            if cnt[num] == 0: continue
            if cnt[2*num] == 0: return []
            ans += [num]
            if num == 0 and cnt[num] <= 1: return []
            cnt[num] -= 1
            cnt[2*num] -= 1
        
        return ans
        
# Solution:
# Runtime: 3422 ms, faster than 11.28% of Python3 online submissions for Find Original Array From Doubled Array.
# Memory Usage: 32.7 MB, less than 55.78% of Python3 online submissions for Find Original Array From Doubled Array.
