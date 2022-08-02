def evalPostfix(text):
    s = Stack()
    for symbol in text:
        if symbol in "0123456789":
            s.push(int(symbol))
        if not s.is_empty():
            if symbol == "+":
                plus = s.pop() + s.pop()
            if symbol == "-":
                plus = s.pop() - s.pop()
            if symbol == "*":
                plus = s.pop() * s.pop()
            if symbol == "/":
                plus = s.pop() / s.pop()


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
