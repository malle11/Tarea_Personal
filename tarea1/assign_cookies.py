class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        niño = 0
        galleta = 0

        while niño < len(g) and galleta < len(s):
            if s[galleta] >= g[niño]:
                niño += 1

            galleta += 1

        return niño
