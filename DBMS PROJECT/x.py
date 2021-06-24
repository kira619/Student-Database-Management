#infix to prefix
def infixTOprefix(exp):
    opression_stack = []
    expression_stack = []
    ops = set(['+', '-', '*', '/', '(', ')'])
    prefix = {'+':1, '-':1, '*':2, '/':2}
    for x in exp:
        if not x in ops:
            expression_stack.append(x)
        elif x == '(':
            opression_stack.append(x)
        elif x == ')':
            while opression_stack[-1] != '(':
                op = opression_stack.pop()
                m = expression_stack.pop()
                b = expression_stack.pop()
                expression_stack.append( op+b+m )
            opression_stack.pop() # pop '('
        else:
            while opression_stack and opression_stack[-1] != '(' and prefix[x] <= prefix[opression_stack[-1]]:
                op = opression_stack.pop()
                m = expression_stack.pop()
                b = expression_stack.pop()
                expression_stack.append( op+b+m )
            opression_stack.append(x)
    
    # leftover
    while opression_stack:
        op = opression_stack.pop()
        m = expression_stack.pop()
        b = expression_stack.pop()
        expression_stack.append( op+b+m )
    print(f'Prefix Expression: {expression_stack[-1]}')
    return expression_stack[-1]
cd = input("Enter the Infix expression: ")
pre = infixTOprefix(cd)