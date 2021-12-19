
# convert from postfix to infix
def postfix_to_infix(postfix):
    stack = []
    for j in range(len(postfix)) :
        if (postfix[j] >='A' and postfix[j] <= 'Z') or (postfix[j] >='a' and postfix[j] <= 'z') :
            stack.append(postfix[j])
        else :
            op1=stack.pop()
            op2=stack.pop()
            stack.append("(" + op2 + postfix[j] + op1 + ")")
    return stack[0]       
