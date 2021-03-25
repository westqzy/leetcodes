#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
import math
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        L_to_R = list(range(L, R+1))
        L_to_R_0b = list(map(bin, L_to_R))
        L_to_R_0b = [i[2:] for i in L_to_R_0b]
        length = [i.count("1") for i in L_to_R_0b]
        hash1 = {}
        for i in length:
            hash1[i] = hash1.get(i, 0 ) + 1
        length = set(length)
        res = 0
        for i in length:
            if i != 1:
                n = int(math.sqrt(i))
                j = 2
                while j <= n:
                    if i % j == 0:
                        break 
                    else:
                        j += 1
                else:
                    res += hash1[i]
        
        return res
                


# @lc code=end
import math
L = 6
R = 10
L_to_R = list(range(L, R+1))
L_to_R_0b = list(map(bin, L_to_R))
L_to_R_0b = [i[2:] for i in L_to_R_0b]
length = [i.count("1") for i in L_to_R_0b]
hash1 = {}
for i in length:
    hash1[i] = hash1.get(i, 0 ) + 1
length = set(length)
res = 0
for i in length:
    n = int(math.sqrt(i))
    j = 2
    if i != 1:
        while j < i:
            if i % j == 0:
                break 
            else:
                j += 1
        else:
            res += hash1[i]
        
print(hash1)       
print(res)


class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in xrange(L, R+1))
