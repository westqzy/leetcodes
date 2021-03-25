#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        typed = typed + "?"
        name = name + "?"
        j = 0
        split_list = []
        for i in range(1, len(typed)):
            if typed[i] != typed[i-1]:
                split_list.append(typed[j:i])
                j = i
        j = 0
        name_list = []
        for i in range(1, len(name)):
            if name[i] != name[i-1]:
                name_list.append(name[j:i])
                j = i
        print(name_list, split_list)
        if len(split_list) != len(name_list):
            return False
        else:
            for i in range(len(name_list)):
                if name_list[i][0] == split_list[i][0] and len(name_list[i]) <= len(split_list[i]):
                    pass
                else:
                    return False
        return True

        
        


# @lc code=end
name = "aleex"+ "?"
typed = "aaleexaa" + "?"
j = 0
split_list = []
for i in range(1, len(typed)):
    if typed[i] != typed[i-1]:
        split_list.append(typed[j:i])
        j = i
j = 0
name_list = []
for i in range(1, len(name)):
    if name[i] != name[i-1]:
        name_list.append(name[j:i])
        j = i

print(name_list)