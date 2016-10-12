## Valid Parentheses
> * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

> * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not

-------
## 特殊输入
> * 空字符串
> * 单字符串，如'['

## 解决思路：利用堆栈,先进后出特性，遇到左括号进栈，遇到右括号则判断当前栈顶是否与之匹配，是，则弹出，否则括号不匹配
