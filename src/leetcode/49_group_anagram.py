class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in anagram_dict.keys():
                anagram_dict[sorted_string] = [string]
            else:
                anagram_dict[sorted_string].append(string)

        return [value for key, value in anagram_dict.items()]

s = Solution()
value_list = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(value_list)
