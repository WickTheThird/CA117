#!/usr/bin/env python3

import sys
import operator
variables = {}

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
    "=": 0
}

def define(listy):
    listy = listy[1:]
    variables[listy[0]] = listy[1]

def calculate(lines):
    lines = lines[1:]
    signs = '+-=/%^*'
    for word in lines:
        if word not in variables and word not in signs:
            return " ".join(lines) + " " + 'unknown'
        elif word in variables and word not in signs:
            pass
    return 'Yes'

def operate(equation):
    global variables
    equation = equation[1:]
    signs = [x for x in equation if x in '+-=/%^*']
    values_e = [y for y in equation if y not in '+-=/%^*']
    total = ops[signs[0]](int(variables[values_e[0]]), int(variables[values_e[1]]))
    values_e = values_e[2:]
    signs = signs[1:]
    i = 0
    while i + 1 < len(signs) and signs != "=" and len(values_e) > 0:
        total = ops[signs[i]](total, int(variables[values_e[i]]))
        i += 1
    for y in variables:
        if int(variables[y]) == total:
            return " ".join(equation) + " " + y
    return " ".join(equation) + " " + 'unknown'


for x in sys.stdin:
    x = x.strip().lower().split()
    if x[0] == 'def':
        define(x)
    elif x[0] == 'calc':
        values = calculate(x)
        if x[2] == '=':
            if x[1] in variables:
                print(x[1] + ' = ' + x[1])
            elif x[1] not in variables:
                print(x[1] + ' = ' + 'unknown')
        elif values != 'Yes':
            print(values)
        elif values == 'Yes':
            print(operate(x))
    elif x[0] == 'clear':
        variables = {}
