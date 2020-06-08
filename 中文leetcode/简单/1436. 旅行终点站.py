'''
给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，
其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。

题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

 
示例 1：

输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo"
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。
本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。
示例 2：

输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。
示例 3：

输入：paths = [["A","Z"]]
输出："Z"
 

提示：

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
所有字符串均由大小写英文字母和空格字符组成。

'''

'''
思路：
1。即没有任何可以通往其他城市的线路的城市重点是这句，那么题目实际上就是找终点中的哪个一个地点，没有出现在起点位置。
2。在终点集合中出现却没在起点集合中出现的元素就是我们要找的结果
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        transpose = list(zip(*paths))  # 将原paths转置，这样第一行存储所有的起点，第二行存储所有终点
        for bb in transpose[1]:  # 遍历每一个终点，如果该终点没有在起点中出现过，说明它就是最终的终点
            if bb not in transpose[0]:
                return bb



class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)
        begin = set()  # 存储所有起点
        end = set()  # 存储所有终点
        for i in range(n):
            begin.add(paths[i][0])
            end.add(paths[i][1])
        where = list(end - begin)  # 集合的差集运算
        return where[0]

