class Hodim:
    def __init__(self, id, name, position, number):
        self.id = id
        self.name = name
        self.position = position
        self.number = number

    def update_info(self, name=None, position=None, number=None):
        self.name = name if name!=None else self.name
        self.position = position if position!=None else self.position
        self.number = number if number!=None else self.number

    def show_info(self):
        print(f"""Hodim:\nID: {self.id},\
              \nName: {self.name},\
              \nPosition: {self.position},\
              \nNumber: {self.number}\n\
              """)
    
    def __repr__(self):
        return f"<class Hodim: {self.id} | {self.name}>"


class Hodimlar:
    def __init__(self):
        self.update_employee_list()

    def update_employee_list(self, rewrite=False):
        if rewrite:
            with open("hodimlar.txt", "w") as f:
                for hodim in self.hodimlar:
                    data = [str(hodim.id), hodim.name, hodim.position, hodim.number]
                    if self.hodimlar[-1]==hodim:
                        f.write(" | ".join(data))
                    else:
                        data.append("\n")
                        f.write(" | ".join(data))
        else:
            self.hodimlar = []
            with open("hodimlar.txt", "r") as f:
                for i in f.read().split("\n"):
                    hodim = i.split(" | ")
                    self.hodimlar.append(Hodim(int(hodim[0]), hodim[1], hodim[2], hodim[3]))

    def find_employee(self, id=None, number=None):
        for hodim in self.hodimlar:
            if (hodim.id==id) or (hodim.number==number):
                return hodim
        return -1

    def show_all_employee(self):
        for hodim in self.hodimlar:
            hodim.show_info()
    
    def update_employee_info(self, id=None, number=None):
        employee = self.find_employee(id, number)
        if employee==-1:
            print(f"Hodim{(id, number)} bazada mavjud emas!")
            return -1

        choose = input("Tanlang(name, position, number): ")

        if choose in ['name', 'position', 'number']:
            user_input = input(f"\"{choose.title()}\"ni kiriting: ")
            if choose=="name":
                employee.update_info(name=user_input)
            elif choose=="position":
                employee.update_info(position=user_input)
            elif choose=="number":
                employee.update_info(number=user_input)
        
        self.update_employee_list(rewrite=True)
        return employee

    def add_employee(self, id, name, position, number):
        self.hodimlar.append(Hodim(id, name, position, number))
        self.update_employee_list(rewrite=True)
    
    def delete_employee(self, id=None, number=None):
        employee = self.find_employee(id, number)
        if employee==-1:
            print(f"Hodim{(id, number)} bazada mavjud emas!")
            return -1

        self.hodimlar.remove(employee)
        self.update_employee_list(rewrite=True)


h_baza = Hodimlar()
h_baza.delete_employee(8)
h_baza.add_employee(7, "Ali", "Chairmans", "777777777")
# h_baza.show_all_employee()
# h_baza.update_employee_info(number="996405599").show_info()
