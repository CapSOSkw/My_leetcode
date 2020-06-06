class Solution:
    def uncommonFromSentences(self, A: str, B: str):
        seen = set()

        for i in A.split() + B.split():
            if i not in seen:
                seen.add(i)

            else:
                seen.remove(i)

        return list(seen)


A = "s z z z s"
B = "s z ejt"

print(Solution().uncommonFromSentences(A, B))