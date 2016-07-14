import sys


def define_function(input_list):
    name = str(input_list[0][1:])
    code = input_list[1:]
    names[name] = code


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


#def define_variable():
#    # add checking for values?
#    varname = stack.pop()
#    value = stack.pop()
#    variables[varname] = value


def check_debug():
    global debug
    if len(sys.argv) > 1:
        if sys.argv[1] == 'debug':
            debug = True


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
}

stack = []
names = {}
debug = False


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


def parse_new_function(thing):
    if thing[0] == ':':
        return True


def parse_as_name(thing):
    if thing in names:
        return thing

def evaluate(inputs):
    if isinstance(inputs, str):
        input_list = inputs.split()
    else:
        input_list = inputs
    for entry in input_list:
        function = parse_new_function(entry)
        name = parse_as_name(entry)
        operation = parse_as_operator(entry)
        integer = parse_as_int(entry)
        string = parse_as_string(entry)
        if function:
            define_function(input_list)
            break
        elif name:
            evaluate(names[name])
        elif operation:
            operation()
        elif integer:
            stack.append(integer)
        elif string:
            stack.append(string)


def main():
    check_debug()
    while True:
        user_input = input(">>>: ")
        evaluate(user_input)
        if debug:
            print("Debug mode...")
            print("stack =", stack)
            print("names =", names)


if __name__ == '__main__':
    main()



# Looping - a function that calls a function x number of times
# Typing? Or should I just use Python types?
# Maybe draw out some sort of control flow, or explicit declaration of how the interpreter needs to "think"


# prefix language = pre order traversal
# vs in order traversal (lisp) vs ???


