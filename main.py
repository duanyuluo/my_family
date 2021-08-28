# encoding=utf-8

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

class Family(object):
    def __init__(self) -> None:
        super().__init__()
        self.members = []

    def add_person(self, new_person):
        self.members.append(new_person)

    def sum_of(self, item):
        result_data = 0
        for member in self.members:
            result_data += getattr(member, item)
        return result_data

    def avg_of(self, item):
        return self.sum_of(item) / len(self.members)

    def who_big(self, item):
        big_person = None
        for member in self.members:
            if big_person == None:
                big_person = member
            elif getattr(member, item) > getattr(big_person, item):
                big_person = member
        return big_person

    def start_work(self):
        for member in self.members:
            if type(member) is Accountor:
                member.start_account()
            elif type(member) is Prgrammor:
                member.start_code()

    def start_report(self):
        for member in self.members:
            member.report()
    

my_family = Family()
my_family.add_person(Accountor("mommy", 39, 170))
my_family.add_person(Prgrammor("daddy", 43, 178))
my_family.add_person(Prgrammor("max", 14, 180))
my_family.add_person(Person("grandpa", 74, 173))
my_family.add_person(Person("grandma", 68, 164))
my_family.add_person(Person("grandpa2", 75, 178))
my_family.add_person(Accountor("grandma2", 66, 168))

print("Total age of my family is ", my_family.sum_of("age"))
print("Avg age of my family is", my_family.avg_of("age"))

print("Total height of my family is ", my_family.sum_of("height"))
print("Avg height of my family is", my_family.avg_of("height"))

p = my_family.who_big("height")
print("The most height person is ", p.name, " the value is", p.height)
p = my_family.who_big("age")
print("The most old person is ", p.name, "the value is ", p.age)

my_family.start_report()
my_family.start_work()