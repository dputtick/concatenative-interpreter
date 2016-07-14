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
    if filename[-3:] == '.ci':
        filename = stack.pop()
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
    try:
        thing = int(thing)
    except ValueError:
        return None
    return thing

def parse_as_string(thing):


def parse_as_operator(thing):
    if thing in operations:
        return operations[thing]


def evaluate(input_line):
    input_list = input_line.split()
        for entry in input_list:
            operation = parse_as_operator(entry)
            integer = parse_as_int(entry)
            string = parse_as_string(entry)
            if operation:
                operation()
            elif integer:
                stack.append(integer)
            elif string:


# data types
def main():
    while True:
        user_input = input(">>>: ")
        evaluate(user_input)
        

if __name__ == '__main__':
    main()


# Maybe I need a special exec keyword that switches the interactive interpreter to
# a mode that will execute a file and return the result to the stack. This logic could be used for the interpreter lines as well as 
# for executing a function. Just have a thing that will execute any code block?


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


