# Last updated: 11/13/2025, 6:16:01 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start: int, remain: int):
            if remain == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                # 剪枝：当前数已经大于剩余的和，后面只会更大，直接结束这一层
                if remain < 0:
                    break

                # 去重：同一层中，如果当前数和前一个相同，则跳过
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # 选择 candidates[i]
                path.append(candidates[i])

                # 每个数只能用一次，所以下一层从 i+1 开始
                backtrack(i + 1, remain - candidates[i])

                # 撤销选择
                path.pop()

        backtrack(0, target)
        return res
