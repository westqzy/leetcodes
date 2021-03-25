#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.requests  = []
    def ping(self, t: int) -> int:
        self.requests.append(t)
        res = 0
        for i in range(len(self.requests)-1,-1,-1):
            if self.requests[i] <= t and self.requests[i] >= t-3000:
                res += 1
            else:
                break
        return res


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

# class RecentCounter(object):
#     def __init__(self):
#         self.q = collections.deque()

#     def ping(self, t):
#         self.q.append(t)
#         while self.q[0] < t-3000:
#             self.q.popleft()
#         return len(self.q)

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/number-of-recent-calls/solution/zui-jin-de-qing-qiu-ci-shu-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。