class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0.0, "bonus": 0.0}

    def income(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus
    # @property
    # def income(self):
    #     return self._income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


pos = Position()
pos.name = "Alex"
pos.surname = "Ivanov"
pos.position = "Manager"
pos.income(30000, 10000)

fullname = pos.get_full_name()

print(fullname)
print(pos.position)
print(pos.get_total_income())
