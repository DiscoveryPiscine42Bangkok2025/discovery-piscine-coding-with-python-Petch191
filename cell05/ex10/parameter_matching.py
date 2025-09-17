import sys
x = len(sys.argv)
if x==1:
    print('none')
else:
    hello = input('What was the parameter? ')
    if hello != "Hello":
        print("Nope sorry...")
    else:
        print('Good job!')