from stack import Stack
class Solution(object):
    def __init__(self):
        self.stack = Stack()
        self.parenthesisSet = (
            ("(",")"),("{","}"),("[","]")
        )
        self.leftParenthesis = ('(','{','[')
        self.rightParenthesis = (')','}',']')

    def isValid(self, s):
        length = len(s)
        if length == 0 or length % 2 != 0:
            return False
        else:
            for letter in s:
                if letter in self.leftParenthesis:
                    self.stack.push(letter)
                elif letter in self.rightParenthesis:
                    if not self.stack.isEmpty() and (self.stack.top(),letter) in self.parenthesisSet:
                        self.stack.pop()
                        continue
                    else:
                        return False
        return self.stack.isEmpty()