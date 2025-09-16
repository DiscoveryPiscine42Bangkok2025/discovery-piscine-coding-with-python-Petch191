try:
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def divide(x,y):
        return x/y
    def multi(x,y):
        return x*y
    first_number =  int(input("Give me the first number = "))
    second_number = int(input("Give me the second number = "))
    print(str(first_number)+" + "+str(second_number)+" = "+str(add(first_number,second_number)))
    print(str(first_number)+" - "+str(second_number)+" = "+str(sub(first_number,second_number)))
    try:
        print(str(first_number)+" / "+str(second_number)+" = "+str(divide(first_number,second_number)))
    except:
         print('Sorry ! You are dividing by zero ')
    print(str(first_number)+" x "+str(second_number)+" = "+str(multi(first_number,second_number)))
except:
    print("Error")
