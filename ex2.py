from datetime import date

class Worker:

    def __init__(self, name, surname, zp):
        self.name = name
        self.surname = surname
        self.zp = zp

    def date_of_relax(self, day, month, year):
        self.day_of_relax = date(year, month, day)
        return self.day_of_relax


class Frontend(Worker):
    
    def __init__(self, name, surname, zp, experience):
        super().__init__(name, surname, zp)
        self.experience = experience

    @staticmethod
    def vizualize():
        return 'Making visual appearance of project'


class Backend(Worker):
    
    def __init__(self, name, surname, zp, experience):
        super().__init__(name, surname, zp)
        self.experience = experience

    @staticmethod
    def set_up_db():
        return 'Setting up database of project'


class Management(Worker):
    def __init__(self, name, surname, zp, rank):
        super().__init__(name, surname, zp)
        self.rank = rank

    @classmethod
    def fire(self, person):
        self.person = person
        if self.person.__class__.__name__ == 'Backend' and 'Frontend':
            del(self.person)
            print('Удалено!')
        else:
            print('Удаление невозможно!')         

        
class Project:
    def __init__(self, manager):
        self.manager = manager
        self.lst_of_backend = []
        self.lst_of_frontend = []

    def add_to_lst_back(self, *args):
        for i in args:
            self.lst_of_backend.append(i)
        return self.lst_of_backend

    def add_to_lst_front(self, *args):
        for i in args:
            self.lst_of_frontend.append(i)
        return self.lst_of_frontend

    def check_backend(self):
        for i in self.lst_of_backend:
            print(i.name, Backend.set_up_db())

    def check_frontend(self):
        for i in self.lst_of_frontend:
            print(i.name, Frontend.vizualize())

manager = Management('Kristina', 'Novikova', 25000, 'HR-manager')
frontender_high = Frontend('Liza', 'Bethowen', 25000, 'Senior')
frontender_1 = Frontend('Mike', 'Luwik', 15000, 'Junior')
frontender_2 = Frontend('Jake', 'Peterson', 20000, 'Middle')
backender_high = Backend('Jason', 'Shark', 30000, 'Senior')
backender_1 = Backend('Billie', 'Brown', 23000, 'Middle')
backender_2 = Backend('Sezim', 'Kim', 20000, 'Junior')
backender_3 = Backend('Sezimka', 'Kimli', 20000, 'Junior')

Management.fire(backender_3)
Management.fire(manager)

project_1 = Project(manager)
project_1.add_to_lst_back(backender_high, backender_1, backender_2)
project_1.add_to_lst_front(frontender_high, frontender_1, frontender_2)
project_1.check_backend()
project_1.check_frontend()