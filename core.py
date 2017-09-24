import argparse


class Instance():

    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.sub,
            "*": self.mult,
            "/": self.div,
            "clr": self.clr,
            "print": self.printer,
            "dupl": self.dupl,
            "drop": self.drop,
            "swap": self.swap,
        }

    def run_once(self, stack, command):
        return self.evaluate(stack, command)

    def evaluate(self, stack, word):
        if word in self.operations:
            method = self.operations[word]
            stack = method(stack)
        else:
            stack.append(word)
        return stack

    def clr(self, stack):
        stack.clear()
        return stack

    def dupl(self, stack):
        if stack:
            stack.append(stack[-1])
        return stack

    def drop(self, stack):
        stack.pop()
        return stack

    def swap(self, stack):
        stack[-1], stack[-2] = stack[-2], stack[-1]
        return stack

    def printer(self, stack):
        if stack:
            print(stack.pop())
        else:
            print("Stack is empty")
        return stack

    def add(self, stack):
        stack.append(str(int(stack.pop()) + int(stack.pop())))
        return stack

    def sub(self, stack):
        stack.append(str(int(stack.pop()) - int(stack.pop())))
        return stack

    def mult(self, stack):
        stack.append(stack.pop() * stack.pop())
        return stack

    def div(self, stack):
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
        return stack


# def execute():
#         filename = stack.pop()
#         if filename[-3:] == '.ci':
#             with open(filename) as f:
#                 file_contents = list(f)
#             for line in file_contents:
#                 evaluate(line)


def parse_args():
    pass


def run_single_instance(code_list):
    instance = Instance()
    stack = []
    for word in code_list:
        stack = instance.run_once(stack, word)
    return stack.pop()


def main():
    parse_args()
    instance = Instance()
    instance.run_once()


if __name__ == '__main__':
    main()
