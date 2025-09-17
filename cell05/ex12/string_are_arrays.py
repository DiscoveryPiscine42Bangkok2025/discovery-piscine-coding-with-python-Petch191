import sys
if len(sys.argv) < 2:
    print('none')
else:
    text = sys.argv[1]
    found = False
    for c in text:
        if c.lower() == 'z':
            print(c, end='')  
            found = True
    if not found:
        print('none')
