def is_opposite_bracket(opening_bracket, closing_bracket) -> bool:
        match opening_bracket:
            case '{': return closing_bracket == '}'
            case '[': return closing_bracket == ']'
            case '(': return closing_bracket == ')'
            case _: return False

def is_closing_bracket(bracket: str) -> bool:
    return bracket in ('}', ']', ')')

class Solution:
    def isValid(self, s: str) -> bool:

        bracket_stack = []

        for bracket in s:
            if not is_closing_bracket(bracket):
                bracket_stack.append(bracket)
            else:
                if not bracket_stack:
                    return False

                opening_bracket = bracket_stack.pop()
                
                if not is_opposite_bracket(opening_bracket, bracket):
                    return False
                
        return len(bracket_stack) == 0
            