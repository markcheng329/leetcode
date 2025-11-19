# Last updated: 11/19/2025, 1:33:02 AM
class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = ""

        for i in range(len(s)):
            if s[i].isdigit():
                # 多位数字：例如 "12[a]"
                cur_num = cur_num * 10 + int(s[i])
            elif s[i] == '[':
                # 进入新的一层：保存当前状态
                num_stack.append(cur_num)
                str_stack.append(cur_str)
                # 重置
                cur_num = 0
                cur_str = ""
            elif s[i] == ']':
                # 当前层结束：弹出上一层信息
                k = num_stack.pop()
                prev_str = str_stack.pop()
                # 上一层字符串 + 当前层重复 k 次
                cur_str = prev_str + cur_str * k
            else:
                # 普通字母
                cur_str += s[i]

        return cur_str