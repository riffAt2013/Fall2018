STACK = []

while True:
    C = input()
    if C == '(':
        STACK += [C]
    if C == ')':
        if len(STACK) > 0:  #avoiding indexOutOfBounds style error
            del STACK[len(STACK)-1]
        else:
            STACK += [C]
    if C == '':
        break 

# Check if push-pop resulted in any extras, if so then Unbalanced
if len(STACK) == 0:
    print('Paranthese Balanced')
else:
    print('Paranthese Unbalanced')
