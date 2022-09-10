# Question: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

# Solution:
class Solution:
    def numberOfWeakCharacters(self, X):
        X = sorted(X)
        n = len(X)
        ans, d, max_y = 0, defaultdict(list), -1
 
        for a, b in X:
            d[a] += [b]
            
        for t in sorted(list(d.keys()))[::-1]:
            for q in d[t]:
                if q < max_y: ans += 1
            for q in d[t]:
                max_y = max(max_y, q)
                
        return ans
      
# Verdict:
# Runtime: 5597 ms, faster than 5.02% of Python3 online submissions for The Number of Weak Characters in the Game.
# Memory Usage: 70.8 MB, less than 9.95% of Python3 online submissions for The Number of Weak Characters in the Game.
