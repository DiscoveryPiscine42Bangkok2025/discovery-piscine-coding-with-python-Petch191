class greet:
    def __init__(self,hello,evo):
        self.hello=hello
        self.evo=evo
    def __str__(self):
        return f"{self.hello} {self.evo}"
print(greet('Hello.','everyone!'))