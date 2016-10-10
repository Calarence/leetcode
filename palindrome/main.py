from stack import Stack
class Solution(object):
    def __init__(self):
        self.stack = Stack()
    def getMiddle(self,collection):
        return len(collection) // 2

    def collector(self,s):
        return [letter for letter in s if letter.isalpha() or letter.isdigit()]

    def pushLetterToStack(self,s):
        collection = self.collector(s)
        middle = self.getMiddle(collection)
        for letter in collection[0:middle]:
            self.stack.push(letter)
        return self.stack,collection,middle

    def isPalindrome(self,s):
        self.stack,collection,middle = self.pushLetterToStack(s)
        print(self.stack.items[0:len(self.stack.items)],collection,middle)
        length = len(collection)
        if length < 2:
            return True
        else:
            if length % 2 == 0 :
                for letter in collection[middle:length]:
                    if self.stack.top().lower() == letter.lower():
                        self.stack.pop()
                        continue
                    else:
                        break
            else:
                for letter in collection[middle+1:length]:
                    if self.stack.top().lower() == letter.lower():
                        self.stack.pop()
                        continue
                    else:
                        break
        return self.stack.isEmpty()










