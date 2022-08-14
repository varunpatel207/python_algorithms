class Solution:
    def topKFrequent(self, nums, k):
        freq_dict = {}
        for num in nums:
            if num not in freq_dict.keys():
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        k_frequent_list = [key for key, value in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)][:k]

        return k_frequent_list

s = Solution()
freq_list = s.topKFrequent([1,1,1,2,2,3,4,4], 2)
print(freq_list)