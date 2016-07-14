import sys


def function_mode(input_list):
    name = input_list[0][1:]
    endvars = index(';')
    local_vars = input_list[1:endvars]
    code = [endvars + 1:]
    function_object = {'locals': local_vars, 'code': code}
    user_functions[name] = function_object


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
    "var": define_variable
}

stack = []
variables = {}
user_functions = {}
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


def parse_as_var(thing):
    if thing in variables:
        return variables[thing]


def parse_as_function(thing):
    if thing in user_functions:
        # call function
    if thing[0] == ':'
        return True


def evaluate(input_line):
    input_list = input_line.split()
    for entry in input_list:
        function_definition = parse_as_function(entry)
        operation = parse_as_operator(entry)
        var = parse_as_var(entry)
        integer = parse_as_int(entry)
        string = parse_as_string(entry)
        if function:
            function_mode(input_list)
        elif operation:
            operation()
        elif var:
            stack.append(var)
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
            print("Debug mode...stack =", stack)


if __name__ == '__main__':
    main()





# How do I deal with variables and the stack? How does Python do it?
# Maybe a pointer to a location in the stack? But then it isn't a stack?
# Looping - just a goto in a list?
# Functions - maybe put arguments into a local dict and then create a list of instructions to loop through
# Typing? Or should I just use Python types?
# Maybe draw out some sort of control flow, or explicit declaration of how the interpreter needs to "think"


# prefix language = pre order traversal
# vs in order traversal (lisp) vs ???


