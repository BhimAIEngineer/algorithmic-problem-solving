class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = 0
        right_remove = 0

        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, path, balance, left_remove, right_remove):
            if index == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add(''.join(path))
                return

            c = s[index]

            if c == '(':
                if left_remove > 0:
                    dfs(index + 1, path, balance, left_remove - 1, right_remove)

                path.append(c)
                dfs(index + 1, path, balance + 1, left_remove, right_remove)
                path.pop()

            elif c == ')':
                if right_remove > 0:
                    dfs(index + 1, path, balance, left_remove, right_remove - 1)

                if balance > 0:
                    path.append(c)
                    dfs(index + 1, path, balance - 1, left_remove, right_remove)
                    path.pop()

            else:
                path.append(c)
                dfs(index + 1, path, balance, left_remove, right_remove)
                path.pop()

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)
