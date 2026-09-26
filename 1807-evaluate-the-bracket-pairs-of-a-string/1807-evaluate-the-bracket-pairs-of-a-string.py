from typing import List

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        lookup = {k: v for k, v in knowledge}
        res = []
        in_bracket = False
        curr_key = []
        
        for ch in s:
            if ch == '(':
                in_bracket = True
            elif ch == ')':
                key = "".join(curr_key)
                res.append(lookup.get(key, "?"))
                curr_key = []
                in_bracket = False
            elif in_bracket:
                curr_key.append(ch)
            else:
                res.append(ch)
                
        return "".join(res)