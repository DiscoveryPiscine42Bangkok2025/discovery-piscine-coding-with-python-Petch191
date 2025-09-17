import sys
x = len(sys.argv)-1
if x==0:
    print('none')
else:
    start = int(sys.argv[1])
    end =  int(sys.argv[2])
    number = list(range(start,end+1))
    print(number)