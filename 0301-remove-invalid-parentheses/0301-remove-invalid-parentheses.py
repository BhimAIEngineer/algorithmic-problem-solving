class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0
        right = 0

        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        result = []

        def dfs(start, left_remove, right_remove, balance, path):
            if start == len(s):
                if balance == 0:
                    result.append(''.join(path))
                return

            c = s[start]

            if c == '(':
                if left_remove > 0:
                    dfs(start + 1, left_remove - 1, right_remove, balance, path)

                path.append(c)
                dfs(start + 1, left_remove, right_remove, balance + 1, path)
                path.pop()

            elif c == ')':
                if right_remove > 0:
                    dfs(start + 1, left_remove, right_remove - 1, balance, path)

                if balance > 0:
                    path.append(c)
                    dfs(start + 1, left_remove, right_remove, balance - 1, path)
                    path.pop()

            else:
                path.append(c)
                dfs(start + 1, left_remove, right_remove, balance, path)
                path.pop()

        dfs(0, left, right, 0, [])

        return list(set(result))