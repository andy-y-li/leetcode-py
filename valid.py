#! /usr/bin/env python

def isValid(s):
    stack = []
    paren_map = {')':'(',']':'[','}':'{'}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

def main(s):
    print isValid(s)

if __name__ == '__main__':
    s = '([]){}'
    main(s)
