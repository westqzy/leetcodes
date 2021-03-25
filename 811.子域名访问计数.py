#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash1 = {}
        for i in cpdomains:
            n = i.split(" ")
            value = int(n[0])
            keys_list = n[1].split(".")
            yuming1 = keys_list[-1]
            yuming2 = keys_list[-2] + "." + keys_list[-1]
            hash1[yuming1] = hash1.get(yuming1, 0) + value
            hash1[yuming2] = hash1.get(yuming2, 0) + value
            if len(keys_list) == 3:
                yuming3 = n[1]
                hash1[yuming3] = hash1.get(yuming3, 0) + value
        return [str(j) + " " + i for i,j in hash1.items()]

            
                
        
# @lc code=end

a = "900 google.mail.com"
b = a.split(" ")[1].split(".")
print(b)