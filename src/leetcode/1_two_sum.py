class Solution:
    def twoSum(self, nums, target):
        fp = 0

        for _fp in range(fp, len(nums)):
            print(nums[_fp])
            for _sp in range(_fp + 1, len(nums)):
                if nums[_fp] + nums[_sp] == target:
                    return [_fp, _sp]
                _sp += 1
            _fp += 1

    def twoSum1(self, nums, target):
        dictu = {}
        for i in range(len(nums)):
            if nums[i] not in dictu:
                dictu[nums[i]] = [i]
            else:
                dictu[nums[i]].append(i)
        for i in dictu:
            if i != target - i and target - i in dictu:
                return [dictu[i][0], dictu[target - i][0]]
            elif i == target - i and len(dictu[i]) > 1:
                return [dictu[i][0], dictu[i][1]]


s = Solution()
print(s.twoSum1([2,5,5,11], 10))
