# Last updated: 12/27/2025, 12:21:53 AM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        res= []
6        for s in strs:
7            res.append(str(len(s)) + "#" + s)
8        return "".join(res)
9        
10
11    def decode(self, s: str) -> List[str]:
12        """Decodes a single string to a list of strings.
13        """
14        #  "5#abcde3#abc"
15        res = []
16        i = 0
17        while i < len(s):
18            j = i
19            while s[j] != "#":
20                j +=1
21            length = int(s[i:j])
22            i = j+1
23            j = i + length
24            res.append(s[i:j])
25            i = j
26        return res
27        
28
29
30# Your Codec object will be instantiated and called as such:
31# codec = Codec()
32# codec.decode(codec.encode(strs))