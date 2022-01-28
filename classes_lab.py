import re


class Person:
    # __mood: str
    # __health_rate: str
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money=0, health_rate=100):

        # user can set the person mood and health for the first time, then his "sleep hours" controls his mood,
        self.mood = Person.moods[0]
        self.__health_rate = health_rate

        self.name = name
        self.money = money

    # user can set the person mood for the first time, then his "sleep hours" controls his mood
    def sleep(self, hours):
        if hours < 7:
            self.__mood = Person.moods[1]
        elif hours > 7:
            self.__mood = Person.moods[2]
        else:
            self.__mood = Person.moods[0]
        print(f"{self.name} is sleeping {hours}\nHe is {self.mood}")

    def eat(self, meals):
        print(f"{self.name} is eating")
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50
        else:
            self.health_rate = 0

    def buy(self, items):
        if self.money >= (10 * items):
            self.money -= (10 * items)
        else:
            print(f"Sorry this buying cannot be completed, "
                  f"{self.name} don't have enough money!")

    @property
    def mood(self):
        return self.__mood

    # user can set the person mood for the first time, then his "sleep hours" controls his mood => can't set it externally
    @mood.setter
    def mood(self, mood):
        self.__mood = mood

    @property
    def health_rate(self):
        return self.__health_rate

    @health_rate.setter
    def health_rate(self, health):
        if health < 0 or health > 100:
            print("health should be between 0 and 100\nHealth set to 100 !")
            self.__health_rate = 100
        else:
            self.__health_rate = health

    def __str__(self):
        return f"Person name:\t{self.name}\nHe is:\t{self.mood} with {self.health_rate} health" \
               f"\nHe have:\t{self.money}LE"


class Employee(Person):
    # __salary: int

    def __init__(self, emp_id, name, money, mood, health_rate, car, email, salary, distance_to_work):
        super().__init__(name=name, money=money, health_rate=health_rate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distance_to_work

    # user can set the person mood for the first time, then his "working hours" controls his mood => can't set it externally
    def work(self, hours):
        print(f"{self.name} is working now")
        if hours > 8:
            self.mood = Person.moods[2]
        elif hours < 8:
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[0]

    def drive(self):
        print(f"{self.name} is driving now")

    def refuel(self):
        print(f"{self.name} is refueling his {self.car} now")

    def send_mail(self, to, subject_name, msg, receiver_name):
        print(f"sending mail from {self.email}")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount >= 1000:
            self.__salary = amount
        else:
            self.__salary = 1000
            print("Cannot set salary value less than 1000 LE\n"
                  "Salary is set to 1000")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, mail):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(regex, mail):
            self.__email = mail
        else:
            print("Invalid mail cannot be set")
            self.__email = "NULL"


class Office:

    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        print(f"employees:{self.employees}")

    def get_employee(self):
        print("getting employee", self)

    def hire(self):
        print("hiring employee", self)

    def fire(self):
        print("firing employee", self)

    def calculate_lateness(self):
        print("calculating lateness", self)

    def deduct(self):
        print("deducting", self)

    def reward(self):
        print("rewarding", self)


class Car:

    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity

    def run(self):
        print("running")

    def stop(self):
        print("stopping")
