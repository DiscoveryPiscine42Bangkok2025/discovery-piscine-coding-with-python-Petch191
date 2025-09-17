import sys
x = len(sys.argv)-1
if x==0:
    print('none')
else:
    count = sys.argv[1:]
    print(f"parameter : {len(count)}")
    for i in count:
        print(f"{i}: {len(i)}")