#
# @lc app=leetcode.cn id=1603 lang=python3
#
# [1603] 设计停车系统
#

# @lc code=start
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park_now = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.park_now[carType-1] -= 1
        return  self.park_now[carType-1] >= 0



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
# @lc code=end

