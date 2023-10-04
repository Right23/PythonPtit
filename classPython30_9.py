## 9.1
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#     def describe(self):
#         print(self.name, self.cuisine_type)
#     def open_restaurant(self):
#         print(self.name+" is open")

# if __name__ == '__main__':
#     r = Restaurant("PT", "SEA FOOD")
#     r.describe()
#     r.open_restaurant()
## 9.2
# r1 = Restaurant("A", "PORK")
# r2 = Restaurant("B", "BEEF")
# r3 = Restaurant("C", "CHICKEN")
# r1.describe()
# r2.describe()
# r3.describe()


# 9.3
class User:
    def __init__(self, fi_name, ls_name, age, job):
        self.fi_name = fi_name
        self.ls_name = ls_name
        self.age = age
        self.job = job
    def greet_user(self):
        print("Hello" +" "+ self.fi_name + " "+self.ls_name)
    def describe(self):
        print('{} {} {} {}'.format(self.fi_name, self.ls_name, self.age, self.job))

# u1=User('John', ' Cena', 47,'wrestler') # object instantiation
# u2=User('Minh', 'Nguyen', 20, 'Student')
# u3=User('The', 'Rock', 50, 'actor')
# u1.describe()
# u1.greet_user()
# u2.describe()
# u2.greet_user()
# u3.describe()
# u3.greet_user()

## 9.4
# class Restaurant:
#     def __init__(self, name, cuisine_type, number_served):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served
#     def describe(self):
#         print(self.name, self.cuisine_type, self.number_served)
#     def open_restaurant(self):
#         print(self.name+" is open")
#     #
#     def set_number_served(self, num):
#         self.number_served = num
#     def increment_number_served(self, num):
#         self.number_served += num
# r1 = Restaurant("A", "SEA", 0)
# r1.describe()
# r1.set_number_served(50)
# r1.describe()
# r1.increment_number_served(50)
# r1.describe()

# # 9.5
# class User:
#     def __init__(self, fi_name, ls_name, age, job, login_attempts):
#         self.fi_name = fi_name
#         self.ls_name = ls_name
#         self.age = age
#         self.job = job
#         self.login_attempts = login_attempts
#     def describe(self):
#         print('{} {} {} {} {}'.format(self.fi_name, self.ls_name, self.age, self.job, self.login_attempts))
#     def increment_login_attempts(self):
#         self.login_attempts +=1
#     def reset_login_attempts(self):
#         self.login_attempts = 0
# u1 = User("Hoa", "Luong", 20, "Student", 1)
# u1.describe()
# u1.increment_login_attempts()
# u1.describe()
# u1.increment_login_attempts()
# u1.describe()

# u1.reset_login_attempts()
# u1.describe()

class User:
    def __init__(self, fi_name, ls_name, age, job):
        self.fi_name = fi_name
        self.ls_name = ls_name
        self.age = age
        self.job = job
    def greet_user(self):
        print("Hello" +" "+ self.fi_name + " "+self.ls_name)
    def describe(self):
        print('{} {} {} {}'.format(self.fi_name, self.ls_name, self.age, self.job))
class Admin(User):
    def __init__(self, fi_name, ls_name, age, job):
        super().__init__(fi_name, ls_name, age, job)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileages(self):
        for i in self.privileges:
            print('admin' ,i , sep=" ")


a = Admin("user","user",20,"user")
a.show_privileages()




