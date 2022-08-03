class Evaluate:

    def __init__(self, Z):
        self.top = -1
        self.size_of_stack = Z
        self.stack = []

    def is_Empty(self):
        if self.top == -1:
            return True
        else: 
            return False


    def pop(self):
        if not self.isEmpty():
            self.stack.pop()


    def push(self, oprand):
        if self.top != self.size_of_stack - 1:
             self.stack.append(oprand)

    def validate_postfix_expression(self, expression):

        v = 0
        w = 0
        for element in exp:
            if element.isnumeric():
                v = v + 1
            else:
                w = w + 1
        if w == v - 1:
            return True
        else:
            return False


     def evaluate_Postfix_expression(text):
        s = Stack()
        for symbol in text:
            if symbol in text:
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
postfix_expression = input() # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
     print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
