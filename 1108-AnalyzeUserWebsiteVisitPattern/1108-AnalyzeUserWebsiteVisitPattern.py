# Last updated: 11/12/2025, 4:57:09 AM
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        data = sorted(zip(timestamp,username,website))

        users = defaultdict(list)
        for i,user,website in data:
            users[user].append(website)
        
        pattern = Counter()
        for user,sites in users.items():
            pattern.update(set(combinations(sites,3)))
        
        return min(pattern, key = lambda x:(-pattern[x],x))