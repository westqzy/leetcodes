#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if 4 > len(s) > 12:
            return []

        def backtrace(index, start):
            if start == len(s) and index == 4:

                ress.append(res[:])

            else:
                for i in range(3):
                    if index != 3:
                        pan = (len(s) - start - i - 1)/(4-index-1)
                        if pan > 3:
                            continue
                    if start >= len(s) or index >= 4:
                        break
                    t = s[start: start + i + 1]
                    if len(t) == 1 or len(t) == 2 and t[0] != "0" or "1"<=t[0]<="2" and 0<=int(t)<=255:
                        res.append(t)
                    else:
                        break
                    backtrace(index+1, start + i +1)
                    res.pop()

        res = []
        ress = []
        backtrace(0, 0)
        ress = [".".join(i) for i in ress]
        return ress
# @lc code=end
s="1122a2"
if not s.isdigit():
    print("er")