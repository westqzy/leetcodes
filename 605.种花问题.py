#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #先找到第一朵花在哪
        # first = -1
        # for i in range(len(flowerbed)):
        #     if flowerbed[i] == 1:
        #         first = i
        #         break
        # else:
        #     if len(flowerbed)%2 == 0:
        #         nmax = len(flowerbed)//2
        #     else:
        #         nmax = len(flowerbed)//2+1
        #     if n <= nmax:
        #         return True
        #     else:
        #         return False
        # list1 = flowerbed[first:]
        # list2 = flowerbed[:first+1]
        # count1 = count2 = 0
        # list2.reverse()
        # for i in range(2,len(list1)):
        #     if i == len(list1)-2 and list1[i-1] == 0 and list1[i] == 0 and list1[i+1] == 0:
        #         list1[i] = 1
        #         count1 += 1
        #     elif i == len(list1)-1 and  list1[i-1] == 0 and list1[i] == 0:
        #         list1[i] = 1
        #         count1 += 1
        #     elif list1[i-1] == 0 and list1[i] == 0 and list1[i+1] == 0:
        #         list1[i] = 1
        #         count1 += 1
        # for i in range(2,len(list2)):
        #     if i == len(list2)-2 and list2[i-1] == 0 and list2[i] == 0 and list2[i+1] == 0:
        #         list2[i] = 1
        #         count2 += 1
        #     elif i == len(list2)-1 and list2[i-1] == 0 and list2[i] == 0:
        #         list2[i] = 1
        #         count2 += 1
        #     elif  list2[i-1] == 0 and list2[i] == 0 and list2[i+1] == 0:
        #         list2[i] = 1
        #         count2 += 1
        # print(count2,count1)
        # return count1 + count2 >= n
        count1 = 0
        if n == 0:
            return True
        if flowerbed == [0] and n == 1:
            return True
        if flowerbed == [1]:
            return False
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count1 += 1
            elif i == len(flowerbed)-2 and flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count1 += 1
            elif i == len(flowerbed)-1 and  flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                count1 += 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count1 += 1
        return count1 >= next


        ####################可以在首尾补0啊啊啊啊啊啊啊啊啊啊啊啊啊啊
# @lc code=end

l = [1,2,3]
print(l[4] == None)