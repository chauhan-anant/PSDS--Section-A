#1. Design an algebraic translation program using a custom operator
# stack that accepts a valid string expression in Infix format (e.g.,
# A+(B*C)) and correctly converts it to Postfix format (e.g.,
# ABC*+).

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(exp):
    stack = []
    postfix = ""

    for ch in exp:

        # If operand
        if ch.isalnum():
            postfix += ch

        # If (
        elif ch == '(':
            stack.append(ch)

        # If )
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()

            if stack:
                stack.pop()

        # If operator
        else:
            while stack and stack[-1] != '(' and \
                  precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()

            stack.append(ch)

    # Empty the stack
    while stack:
        postfix += stack.pop()

    return postfix


exp = input("Enter infix expression: ")

print("Postfix expression:", infix_to_postfix(exp))


# 2. Write an Expression Evaluation program that processes a
# completed string in Postfix format, utilizing an integer stack to
# compute and print the final mathematical output.

def evaluate(postfix):
    stack = []

    for ch in postfix:

        # If number
        if ch.isdigit():
            stack.append(int(ch))

        # If operator
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a // b)

    return stack.pop()


exp = input("Enter postfix expression: ")

print("Result:", evaluate(exp))