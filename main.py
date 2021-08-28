# encoding=utf-8

from person import Person, Accountor, Prgrammor
from family import Family

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