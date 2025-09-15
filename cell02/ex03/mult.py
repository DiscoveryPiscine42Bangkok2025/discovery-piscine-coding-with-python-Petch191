first_num = int(input('Enter the first number: '))
second_num = int(input('Enter the second number: '))
result = first_num * second_num
if result !=0:
    if result < 0:
        print(f"{first_num} x {second_num} = {result}")
        print("The result is negative.")
    else:
        print(f"{first_num} x {second_num} = {result}")
        print("The result is positive.")
else:
    print(f"{first_num} x {second_num} = {result}")
    print("The result is positive and negative.")