#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        yuming_list = [i.split("@") for i in emails]
        for i in range(len(yuming_list)):
            str_alice = yuming_list[i][0]
            j = 0
            while j <= len(str_alice)-1:
                if str_alice[j] == "+":
                    str_alice = str_alice[:j]
                    break
                if str_alice[j] == ".":
                    str_alice = str_alice[:j] + str_alice[j+1:]
                    j -= 1
                j += 1
            yuming_list[i][0] = str_alice
        print(yuming_list)
        reslist = [i[0]+"@"+i[1] for i in yuming_list]
        print(reslist)
        return len(set(reslist))

# @lc code=end
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
yuming_list = [i.split("@") for i in emails]
print(yuming_list)


class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)


