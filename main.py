import re
import ast


class compiler:
    def __init__(self):
        self.__exp = input("Enter expression: ")        # take expression as input
        self.token = self.tokenization()                # call tokenization function
        self.syntaxTree = self.syntaxTree()             # call syntax tree function

    def __str__(self):
        return f"\nToken:\n{self.token}\n\nSyntax Tree:\n{self.syntaxTree}"     # object to print values

    def tokenization(self):
        return list(filter(str.strip, re.split(r"(\W)", self.__exp)))               # create tokens with regex

    def syntaxTree(self):
        return ast.dump(ast.parse(self.__exp), indent=4)               # create syntax tree


if __name__ == "__main__":
    c = compiler()                                      # create object for class
    print(c)                                            # print values (token and syntax tree)
