class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        ob = zip(d.values(), d.keys())
        q = sorted(ob, reverse=True)
        ans = ""
        for j in q:
            ans += j[1]*j[0]
        return ans