#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        cur = 0
        ans = 0
        for i in range(n):
            cur += gas[i]-cost[i]
            total += gas[i]-cost[i]
            if cur < 0:
                cur = 0
                ans = i + 1
        if total < 0:
            return -1
        else:
            return ans


# @lc code=end

gas = [1,2,3,4,5,1,2,3,4,5]
gas = gas + gas
print(gas)