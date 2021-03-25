#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
import math
import collections
class Solution:
    def generate_more(self, a, b, x, y):
        nodes = []
        nodes.append((a, 0))
        nodes.append((0, b))
        nodes.append((x, b))
        nodes.append((a, y))
        if a + b < y:
            nodes.append((0, a+b))
        else:
            nodes.append((a+b-y, y))
        if a + b < x:
            nodes.append((a+b, 0))
        else:
            nodes.append((x, a+b-x))
        return nodes

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # if z > x+y:
        #     return False
        # if z == x or z == y:
        #     return True
        # if z == 0:
        #     return True
        # ma = max(x,y)  
        # mi = min(x,y)
        # if mi == 0 and ma != z:
        #     return False
        # while True:
        #     d = ma - mi
        #     if d <= 0:
        #         return False
        #     if z % d == 0:
        #         return True
        #     a = min(d, mi)
        #     b = max(d, mi)
        #     mi = a
        #     ma = b
        
        # BFS
        if z < 0 or z > x+y:
            return False

        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        visited.add((0, 0))
        while queue:
            a, b = queue.popleft()
            if a == z or b == z or a + b == z:
                return True
            nodes = self.generate_more(a, b, x, y)
            for node in nodes:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
            
        return False



        # if x + y < z:
        #     return False
        # if x == 0 or y == 0:
        #     return z == 0 or x + y == z
        # return z % math.gcd(x, y) == 0
        


            
# @lc code=end
a = 10
b = 0
import math
