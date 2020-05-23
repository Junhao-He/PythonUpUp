# coding = utf-8

"""
Author:hjh
Date:05.23
"""


class Solution(object):
    def four_sum(self, number_list, target):
        length = len(number_list)
        nums = sorted(number_list)
        # nums = number_list
        dict = {}
        result = []
        if length < 4:
            return []
        if length == 4 :
            if sum(nums) == target:
                return [nums]
            else:
                return []
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i]+nums[j] in dict:
                    key = nums[i]+nums[j]
                    dict[key].append((i, j))
                else:
                    key = nums[i]+nums[j]
                    dict[key] = [(i, j)]
        print(dict)
        for p in range(2, length-1):
            for q in range(p+1, length):
                sub = target-nums[p]-nums[q]
                if sub in dict:
                    for index in dict[sub]:
                        if index[1] < p:
                            result.append((nums[index[0]], nums[index[1]], nums[p], nums[q]))
        return list(set(result))

if __name__ == '__main__':
    num_list = [-5,5,4,-3,0,0,4,-2]
    target = 4
    so = Solution()
    print(so.four_sum(num_list, target))




