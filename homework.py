from stack import LStack
operator = ['*', '/', '+', '-']
bracket = ['(', ')']
infix1 = ['3', '*', '(', '4', '+', '10', '/', '2', ')']
infix2 = ['3', '*', '(', '(', '4', '+', '10', ')', '/', '2', ')']

def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def priority(x):
    if (x == '*') | (x == '/'):
        return 2
    else:
        return 1

def change_infix_to_postfix(infix):
    calc = LStack()
    postfix = []
    for i in infix:
        if i == ' ':
            continue
        elif is_number(i):
            postfix.append(i)
        elif i in operator:
            while priority(i) < priority(calc.peek()):
                x = calc.pop()
                if x in operator:
                    postfix.append(x)
            calc.push(i)
        elif i == bracket[0]:
            calc.push(i)
        elif i == bracket[1]:
            while calc.peek() != '(':
                postfix.append(calc.pop())
            calc.pop()

    while calc.size != 0:
        postfix.append(calc.peek())
        calc.pop()
    return postfix

def calculate_postfix(postfix):
    result = LStack()
    for c in postfix:
        if is_number(c):
            result.push(c)
        elif c in operator:
            a = int(result.pop())
            b = int(result.pop())
            if c == '+':
                x = b+a
            elif c == '-':
                x = b-a
            elif c == '*':
                x = b*a
            elif c == '/':
                x = b/a
            else:
                continue
            result.push(x)
    return result.peek()

if __name__ == "__main__":
    postfix1 = change_infix_to_postfix(infix1)
    postfix2 = change_infix_to_postfix(infix2)
    result1 = calculate_postfix(postfix1)
    result2 = calculate_postfix(postfix2)
    print("=======================================")
    print("중위표기법 1 : ", ' '.join(infix1))
    print("후위표기법 1 : ", ' '.join(postfix1))
    print("후위표기법 1 계산 결과 : ", result1)
    print("=======================================")
    print("중위표기법 2 : ", ' '.join(infix2))
    print("후위표기법 2 : ", ' '.join(postfix2))
    print("후위표기법 2 계산 결과 : ", result2)
    print("=======================================")
