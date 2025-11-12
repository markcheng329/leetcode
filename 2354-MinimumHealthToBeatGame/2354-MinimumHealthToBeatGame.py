# Last updated: 11/12/2025, 4:56:53 AM
class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) - min(max(damage),armor) +1
        