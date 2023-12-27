import sqlite3

class Hodimlar:
    def __init__(self):
        self.conn = sqlite3.connect("hodimlar.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = """
        CREATE TABLE hodimlar (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name CHAR(50),
            position CHAR(50),
            phone_number CHAR(50)
        )
        """

        try: 
            self.cursor.execute(query)
            print("Table has been created successfully")
        except Exception as e:
            print(str(e).capitalize())

    def add_employee(self, employee: list):
        
        query = "INSERT INTO hodimlar(name, position, phone_number) VALUES (?,?,?)"

        try: 
            self.cursor.executemany(query, employee)
            self.conn.commit()
            print("Employee has been added successfully")
        except Exception as e:
            print(str(e).capitalize())


    def show_employee(self, id=None, number=None):

        where = "select * from hodimlar where "
        if id:
            query = where + f"id={id}"
        elif number:
            query = where + f"phone_number={number}"
        else:
            query = "select * from hodimlar"

        try: 
            data = self.cursor.execute(query)
            print(*data, sep="\n")
        except Exception as e:
            print(str(e).capitalize())


    def delete_employee(self, id=None, number=None):
        where = "delete from hodimlar where "
        if id:
            query = where + f"id={id}"
        elif number:
            query = where + f"phone_number={number}"

        try: 
            self.cursor.execute(query)
            self.conn.commit()
            print("Employee has been deleted successfully")
        except Exception as e:
            print(str(e).capitalize())

    
    def update_employee_info(self, id=None, number=None):
        choose = input("Tanlang(name, position, phone_number): ")

        if choose in ['name', 'position', 'phone_number']:
            user_input = input(f"\"{choose.title()}\"ni kiriting: ")

            if id:
                query = f"update hodimlar set {choose}={user_input} where id={id};"
            elif number:
                query = f"update hodimlar set {choose}={user_input} where phone_number={number};"

        try: 
            self.cursor.execute(query)
            self.conn.commit()
            print("Employee has been updated successfully")
        except Exception as e:
            print(str(e).capitalize())


h_baza = Hodimlar()
# h_baza.create_table()
h_baza.show_employee()
h_baza.update_employee_info(id=2)
