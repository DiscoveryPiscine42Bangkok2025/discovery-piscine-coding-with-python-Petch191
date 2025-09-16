def f():
    your_float = float(input('Give me a number: '))
    if your_float == int(your_float):
        print("This number a integer.")
    else:
        print("This number an decimal.")
f()