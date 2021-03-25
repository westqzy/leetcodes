#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        self.dict = [0]*n
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.dict[id-1] = value
        res = []
        if self.ptr == id:
            while id <= len(self.dict):
                if self.dict[id-1] != 0:
                    res.append(self.dict[id-1])
                    id += 1
                else:
                    break
            self.ptr += len(res)
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
# @lc code=end

