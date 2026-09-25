from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        exp = []
        for i in range(len(expression)):
            exp.append(expression[i])
            if i + 1 < len(expression):
                c1, c2 = expression[i], expression[i + 1]
                if (c1.isalpha() or c1 == '}') and (c2.isalpha() or c2 == '{'):
                    exp.append('*')
        
        values = []
        ops = []
        
        def apply_op():
            op = ops.pop()
            v2 = values.pop()
            v1 = values.pop()
            if op == ',':
                values.append(v1 | v2)
            elif op == '*':
                values.append({s1 + s2 for s1 in v1 for s2 in v2})
        
        precedence = {',': 1, '*': 2}
        
        for token in exp:
            if token.isalpha():
                values.append({token})
            elif token == '{':
                ops.append('{')
            elif token == '}':
                while ops and ops[-1] != '{':
                    apply_op()
                ops.pop()
            else:
                while ops and ops[-1] != '{' and precedence[ops[-1]] >= precedence[token]:
                    apply_op()
                ops.append(token)
                
        while ops:
            apply_op()
            
        return sorted(list(values[0]))