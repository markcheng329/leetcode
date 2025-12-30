# Last updated: 12/30/2025, 6:03:18 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        res = []
6        for s in strs:
7            res.append(str(len(s)) + "#" + s)
8        return "".join(res)
9
10    def decode(self, s: str) -> List[str]:
11        """Decodes a single string to a list of strings.
12        """
13        res = []
14        i = 0
15
16        while i < len(s):
17            j = i
18            while s[j] != "#":
19                j +=1
20            length = int(s[i:j])
21            i = j +1
22            j = i + length
23            res.append(s[i:j])
24            i = j
25        return res
26
27
28
29# Your Codec object will be instantiated and called as such:
30# codec = Codec()
31# codec.decode(codec.encode(strs))