def add():
    stack.append(stack.pop() + stack.pop())


def sub():
    a = stack.pop()
    b = stack.pop()
    stack.append(a - b)


def mult():
    stack.append(stack.pop() * stack.pop())


def div():
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)