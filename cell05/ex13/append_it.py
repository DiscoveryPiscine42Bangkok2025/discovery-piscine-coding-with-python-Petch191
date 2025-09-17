import sys
import re
x = len(sys.argv)-1
if x ==0:
    print("none")
else:
    ism = sys.argv[1:]
    for i in ism:
        if not re.search("ism",i):
            print(i + "ism")