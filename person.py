# encoding = utf-8

class Person(object):
    def __init__(self, name, age, height) -> None:
        self.age = age
        self.height = height
        self.name = name
        super().__init__()
    
    def report(self):
        print("Yes, sir. This is", self.name)

class Prgrammor(Person):
    def start_code(self):
        print("I start code work...", self.name)
        print("end work")

class Accountor(Person):
    def start_account(self):
        print("I start account work...", self.name)
        print("end work")
