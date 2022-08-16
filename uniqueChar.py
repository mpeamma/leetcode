class Solution:
    def firstUniqChar(self, s):
        buckets = [None for x in range(26)]
        max_len = len(s)
        for idx, c in enumerate(s):
            b = ord(c) - ord('a')
            if buckets[b] is None:
                buckets[b] = idx
            elif buckets[b] < max_len:
                buckets[b] = max_len
        m = min(filter(lambda x: x is not None, buckets))
        if m == max_len:
            return -1
        return m


print(Solution().firstUniqChar("aabbcc"))
