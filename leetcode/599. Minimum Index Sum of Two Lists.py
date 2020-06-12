'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite
restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".



Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).



Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
'''

from collections import Counter, defaultdict

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        l1 = set(list1)
        l2 = set(list2)
        dic = defaultdict(int)
        res = []

        common = l1&l2

        if common.__len__() == 1:
            return list(common)[0]


        for l in [list1, list2]:
            for idx, key in enumerate(l):
                if key in common:
                    dic[key] += idx


        min_value = min(dic.values())

        for key, value in dic.items():
            if value == min_value:
                res.append(key)


        return res




if __name__ == '__main__':
    s = Solution()
    l1 = ["Shogun","Tapioca Express","Burger King","KFC"]

    l2 = ["KFC","Burger King","Tapioca Express","Shogun"]

    print(s.findRestaurant(l1, l2))