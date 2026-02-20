from typing import List, Optional

class Solution:
    def validParentheses(self, s: str) -> bool:
        """
        This function checks if the input string s has valid parentheses.
        A string has valid parentheses if every open parenthesis can be matched with a corresponding close parenthesis.
        """
        # Create a dictionary to map closing parentheses to their corresponding opening ones
        parentheses_map = {")": "(", "}": "{", "]": "["}
        
        # Create a set of opening parentheses for easy lookup
        opening_parentheses = set(["(", "{", "["])
        
        # Create a stack to store the opening parentheses
        stack = []
        
        # Iterate over each character in the string
        for char in s:
            # If the character is an opening parenthesis, push it onto the stack
            if char in opening_parentheses:
                stack.append(char)
            # If the character is a closing parenthesis, check if the stack is empty or the top of the stack does not match with the current closing parenthesis
            elif char in parentheses_map:
                if not stack or stack.pop() != parentheses_map[char]:
                    return False
        
        # If the stack is empty after iterating over the entire string, the parentheses are valid
        return not stack

# --- Test Cases ---
if __name__ == '__main__':
    s = Solution()
    print(s.validParentheses("()"))  # Expected: True
    print(s.validParentheses("()[]{}"))  # Expected: True
    print(s.validParentheses("(]"))  # Expected: False
    print(s.validParentheses("([)]"))  # Expected: False
    print(s.validParentheses("{[]}"))  # Expected: True