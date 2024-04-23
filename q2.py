def check_brackets(s: str) -> str:
    stack = []
    result = [" "] * len(s)
    for i, char in enumerate(s):
        # if it is a left bracket, append its index to the stack
        if char == '(': 
            stack.append(i)
        # if it is a right bracket, check if the stack is empty
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = "?"
    while stack: # if there are unmatched left brackets, mark them as 'x'
        result[stack.pop()] = 'x'

    return ''.join(result)

if __name__ == "__main__":
    test_cases = [
        "bge)))))))))",
        "((IIII))))))",
        "()()()()(uuu",
        "))))UUUU((()"
    ]
    for test_case in test_cases:
        print(check_brackets(test_case))
      