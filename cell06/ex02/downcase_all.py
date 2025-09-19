import sys 
class downcase_all:
    def __init__(self,text):
        self.text = text
    def run(self):
        self.text = sys.argv[1:]
        if not self.text:
            print("none")
        else:
            for i in self.text:
                print(i.lower())
downcase_all('text').run()