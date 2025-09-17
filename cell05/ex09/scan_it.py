import sys
import re
x = len(sys.argv)-1
if x ==0 or x==1:
    print('none')
else:
    text = "".join(sys.argv[1:])
    result = re.findall("the",text)
    if result:
        print(len(result)-1)
    else:
        print('none')