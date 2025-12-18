# Last updated: 12/17/2025, 10:24:59 PM
1class Codec:
2    def encode(self, strs: List[str]) -> str:
3        """Encodes a list of strings to a single string.
4        """
5        # abced = 5#abced
6        res = ""
7        for s in strs:
8            res += str(len(s)) + "#" + s
9        return res
10        
11
12    def decode(self, s: str) -> List[str]:
13        """Decodes a single string to a list of strings.
14        """
15        #5#abced
16        i = 0
17        res = []
18        while i < len(s):
19            j = i
20            while s[j] != "#":
21                j +=1
22            length = int(s[i:j])
23            i = j+1
24            j = i + length
25            res.append(s[i:j])
26            i = j
27        return res
28
29
30        
31
32
33# Your Codec object will be instantiated and called as such:
34# codec = Codec()
35# codec.decode(codec.encode(strs))