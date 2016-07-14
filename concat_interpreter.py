import sys
import os


def add():
    stack.append(stack.pop() + stack.pop())


def sub():
    stack.append(stack.pop() - stack.pop())


def mult():
    stack.append(stack.pop() * stack.pop())


def div():
    stack.append(stack.pop() / stack.pop())


def clr():
    stack.clear()


def printer():
    if stack:
        print(stack[-1])
    else:
        print("Stack is empty")


def dup():
    if stack:
        stack.append(stack[-1])


def drop():
    stack.pop()


def swap():
    stack[-1], stack[-2] = stack[-2], stack[-1]


def exit():
    sys.exit()


def execute():
    filename = stack.pop()
    if filename[-3:] == '.ci':
        with open(filename) as f:
            file_contents = list(f)
        for line in file_contents:
            evaluate(line)


def define_variable():
    # add checking for values?
    varname = stack.pop()
    value = stack.pop()
    variables[varname] = value


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "clr": clr,
    "print": printer,
    "dup": dup,
    "drop": drop,
    "swap": swap,
    "exit": exit,
    "exec": execute,
    "var": define_variable
}

stack = []
variables = {}
user_functions = {}


def parse_as_int(thing):
    # Can I use more fundamental language features to evaluate type of input?
    try:
        thing = int(thing)
    except ValueError:
        return None
    return thing


def parse_as_string(thing):
    # Maybe I can use quotes to recognize a string
    if isinstance(thing, str):
        return thing


def parse_as_operator(thing):
    if thing in operations:
        return operations[thing]


def parse_as_var(thing):
    if thing in variables:
        return variables[variable]


def evaluate(input_line):
    input_list = input_line.split()
    for entry in input_list:
        operation = parse_as_operator(entry)
        var = parse_as_var(entry)
        integer = parse_as_int(entry)
        string = parse_as_string(entry)
        if operation:
            operation()
        elif var:
            stack.append(var)
        elif integer:
            stack.append(integer)
        elif string:
            stack.append(string)


def main():
    while True:
        user_input = input(">>>: ")
        evaluate(user_input)
        

if __name__ == '__main__':
    main()





# How do I deal with variables and the stack? How does Python do it?
# Maybe a pointer to a location in the stack? But then it isn't a stack?
# Looping - just a goto in a list?
# Functions - maybe put arguments into a local dict and then create a list of instructions to loop through
# Typing? Or should I just use Python types?
# Executing files
# Maybe draw out some sort of control flow, or explicit declaration of how the interpreter needs to "think"
# 


# prefix language = pre order traversal
# in order traversal


