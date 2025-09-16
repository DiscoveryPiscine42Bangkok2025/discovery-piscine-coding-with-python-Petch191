import sys
x = len(sys.argv)-1
if x ==0:
    print("none")
elif x==1:
    print("none")
else:
    for i in reversed(sys.argv[1:]):
        print(i)