# temperature = 25
# if temperature > 20:
#         print('Its a warm day')
#         print( 'This line runs regardless of the temperature')

# my_age = 61
# print(my_age)

# my_name = 'Lenton'
# print(my_name)

# is_coder = True
# print(is_coder)

# height_in_meters = 5.60
# print(height_in_meters)

# favourite_colour = 'sky_blue'
# print(favourite_colour)

# book_title = 'intro_to_algebra'
# number_of_page = 250
# print(book_title)

# count = 0
# count = 10
# print(count)

# message = 'goodbye'
# print(message)

# num1 = 5
# num2 = 3
# sum_result = num1 + num2
# print(sum_result)

# greetings = 'Hello'
# name = 'Alice'
# full_greetings = greetings + name
# print(full_greetings)

# quantity = 5
# item_cost = 3.99
# total_cost = quantity*item_cost
# print(total_cost)

# students = 30
# groups = 5
# students_per_group = students/groups
# print(students_per_group)

# year = 1964
# current_year = 2025
# calculated_age = current_year - year 
# print(calculated_age)

# word1 = 'gold'
# word2 = 'smith'
# combined_words = word1 + word2
# print(combined_words)
# y = 1
# x = 2
# print(x+y)

# m = 8
# n = 5
# k = m+n
# print(k)

# # Iluustration of a Function


# def get_total(quantity,price):
#   total=quantity*price
#   return total 

# subtotal = get_total(2,1000)
# print(subtotal)

# a=2
# while a<=10:
#   print(a)
#   a=a+2

#   print(10<9)

# a=200
# b=13
# if b > a:
#    print('b is greater than a')
# else:
  #print('b is not greater than a') 

# grades = [1,2,3,4,5,6,7,8,9,10]
  # find the odd number from the list
# def odd_number(grades):
#       for grade in grades:
#         if grade %2 != 0:
#            print(grade)  
# odd_number(grades)           

# name = 'Josiah'
# def get_user(name):
#     if name == 'Josiah':
#       print('we can manage you')
#     elif name == 'Mr Lenton':
#       print("You're the right one")
#     else:
#       print('We cant make any choice')
# get_user(name)

# age = 30
# def allowable_age():
#     if age>=20 and age<=40:
#       print(" You can gain access to play")
#     else:
#       print(" You can't gain access to play")
# allowable_age()

# nums = [1,2,3,4,5,6,7,8]
# def half(x):
#    return x/2
# def map_list(nums,func):
#   for num in nums:
#     print(func(num))
# map_list(nums,half)

# Classes

#

# class Dog:
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age

#     def dogProfile(self):
#         return f"My dog's name is {self.name} and my age is {self.age} and finally my color is {self.color}"
 
# obj1 = Dog("Bingo", "brown", 4)
# print(obj1.dogProfile())

# class Dog:
#     def __init__(self, name, color, age):
#         self.name = name
#         self.color = color
#         self.age = age

#     def dogProfile(self):
#         return f"My dog's name is {self.name} and my age is {self.age} and finally my color is {self.color}"

# obj1 = Dog("Bingo", "brown", 4)
# print(obj1.dogProfile())  # Explicitly print the result


my_list = ['s', 'u', 'm', 'k']
my_list.append('j')
print(my_list)

my_list = ['a','f','d',5]
my_list.pop(3)
print(my_list)

my_list = ['s', 'u', 'm', 'k']
my_list.extend('s')
print(my_list)

my_list = ['s', 'u', 'm', 'k']
my_list.reverse()
print(my_list)

my_list = ['s', 'u', 'm', 'k']
my_list.('m')
print(my_list)

my_list = ['s', 'u', 'm', 'k']
index = my_list.index('m')
print(index)

my_list = ['s', 's', 's', 'u', 'm', 'k']
count_s = my_list.count('s')
print(count_s)

my_list = ['s', 'u', 'm', 'k']
my_list.remove('m')  # Removes 'm'
print(my_list)  # Output: ['s', 'u', 'k']

my_list = ['s', 'u', 'm', 'k']
del my_list[2]
print(my_list)

    ictinstrcutors = {"kingdavid":"dataanalysis",
 "douglas":"cybersecurity"}
    print(ictinstructors)

    thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

ictinstructors = {"kingdavid": "dataanalysis", "douglas": "cybersecurity"}
print(ictinstructors)

lentonisoks = {
  "name" : "lentonisokariari",
  "dept" : "chemical engineering",
  "matricno" : "de157847m",
  "age" : 36
}
print(lentonisoks)