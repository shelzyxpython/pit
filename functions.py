# class Point3D:
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x=x
#         self.y=y
#         self.z=z
#
#     def info(self):
#         print(f'x =  {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a,b):
#         return b - a
#
#     def distance2(self):
#         return  f'Расстояние от x до y: {self.distance(self.x, self.y)}, \nРассятояние между y и z: {self.distance(self.y, self.z)}'
#
# first = Point3D(4,5,8)
# second = Point3D(5,8,7)
# third = Point3D(8,7,3)
# first.info()
# print(first.distance2())

# class Square:
#
#     def __init__(self, a = 0):
#         self.a=a
#     def info(self):
#         print(f'a =  {self.a}')
#
#     def S(self, a):
#         return a * a
#     def P(self, a):
#         return a * 4
#     def P_and_S(self):
#         return f'Площадь квадрата = {self.S(self.a)} \nПериметр квадрата = {self.P(self.a)}'
#
# first = Square(23)
# second = Square(7654)
# third = Square(0)
# first.info()
# print(first.P_and_S())

# import math
# class triangle:
#
#     def __init__(self, a = 0, b = 0):
#         self.a=a
#         self.b=b
#     def info(self):
#         print(f'a =  {self.a} b = {self.b}')
#
#     def S(self, a,b):
#         return 0.5 * (a * b)
#     def P(self, a,b):
#         c = a**2 + b**2
#         d = a + b + math.sqrt(c)
#         return d
#
#     def P_and_S(self):
#         return f'Площадь треугольника = {self.S(self.a, self.b)} \nПериметр квадрата = {self.P(self.a, self.b)}'
#
# first = triangle(5,3)
# print(first.P_and_S())
#
# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
# class Triangle:
#     def __init__(self, A, B, C):
#         self.A = A
#         self.B = B
#         self.C = C
#     def perimeter(self):
#         AB = self.A.distance(self.B)
#         BC = self.B.distance(self.C)
#         CA = self.C.distance(self.A)
#         return AB + BC + CA
# A = Point(2, 4)
# B = Point(6, 9)
# C = Point(6, 0)
# triangle = Triangle(A, B, C)
# perimeter = triangle.perimeter()
# print(perimeter)

# class CPerson:
#     def __init__(self):
#         self.first_name = ''
#         self.last_name = ''
#         self.middle_name = ''
#
#         self.day = 0
#         self.month = 0
#         self.year = 0
#
#         self.gender = ''
#
#     def __del__(self):
#         print('CPerson удален')
#
#     def FIO(self, first_name, last_name, middle_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#
#     def birthday_date(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def gender_party(self, gender):
#         self.gender = gender
#
# person = CPerson()
#
# person.FIO("Я", "Кажется", "Понял")
# person.birthday_date(30, 5, 2007)
# person.gender_party("Мужской")
#
# name = person.first_name + ' ' + person.middle_name + ' ' + person.last_name
# birth_date = str(person.day) + '.' + str(person.month) + '.' + str(person.year)
# gender = person.gender
#
# print("Ф.И.О:", name)
# print("Дата рождения:", birth_date)
# print("Пол:", gender)

