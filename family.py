#encoding = utf-8

from person import *

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
    