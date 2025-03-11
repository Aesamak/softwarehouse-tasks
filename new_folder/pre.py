def infix_to_postfix(expression):
    # Operator precedence and associativity
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

    stack = []  
    output = []  
    tokens = expression.split() 

    for token in tokens:
        if token.isalnum():  
            output.append(token)
        elif token == '(':  
            stack.append(token)
        elif token == ')':  
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while stack and stack[-1] != '(' and (
                (precedence[token] < precedence[stack[-1]]) or
                (precedence[token] == precedence[stack[-1]] and associativity[token] == 'left')
            ):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

infix_expression = "A + B * C - ( D / E + F ) ^ G"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_expression)
