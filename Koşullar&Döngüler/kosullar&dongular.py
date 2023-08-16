###########################
# KOŞULLAR (Conditions)
###########################

# True-False Hatırlayalım
1 == 1
1 == 2

# if
if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11

if number == 10:
    print("number is 10")

number = 10

def number_check(number):
    if number ==  10:
        print("number is 10")

number_check(12)

# else
def number_check(number):
    if number ==  10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)

# elif
def number_check(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10 ")

number_check(10)

##################
# DÖNGÜLER (LOOPS)
##################
# for loop

students =  ["John", "Mark", "Venessa", "Mariam"]

students[0]
students[1]
students[2]

for student in students:
    print(student.upper()) #upper() harfleri büyüttü

salaries =  [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary*20/100+salary))

for salary in salaries:
    print(int(salary*30/100+salary))

for salary in salaries:
    print(int(salary*50/100+salary))

def new_salary(salary, rate):
    return int(salary*rate/100+salary)

new_salary(2540,13)

for salary in salaries:
    if salary  >= 3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary, 20))

#############################
# Uygulama - Mülakat Sorusu
##############################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz

# before : " hi my name is john and i am learning python"
# after : " Hi mY NaMe iS JoHn aNd i aM LeArNiNg PyThOn"

range(len("miuul"))
range(0,5)

for i in range(0,5):
    print(i)
def alternating(string):
    new_string  = ""
    # girelen string'in indexlerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
            #index tek ise küçük harfe çevir
        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("merhaba ben filiz python ogreniyorum")

############################
# Break & Continue & While
############################

salaries = [1000, 2000, 3000, 4000, 5000]

# break
for salary in salaries:
    if salary == 3000:
        break
    print(salary)

# continue
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)

# while
number = 1
while number < 5:
    print(number)
    number += 1

#########################################################
# Enummerate: Otomatik Counter/ Indexer ile for loop
#########################################################

students =  ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)


for index, student in enumerate(students):
    print(index,student)

A = []
B = []

for index, student in enumerate(students):
   if index % 2 == 0:
       A.append(student)
   else:
       B.append(student)

print(A)
print(B)

###############################
# Uygulama - mülakat sorusu
################################
# divide_students fonksiyonu yazınız.
# çift indexte yer alan öğrencileri bir listeye alınız.
# tek indexte yer alan öğrencileri bir listeye alınız.
# fakat bu iki liste tek bir liste olarak return olsun.

students =  ["John", "Mark", "Venessa", "Mariam"]

def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)

########################################################
# alternating fonksiyonunun enumerate ile yazılması
########################################################
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

    alternating_with_enumerate("merhaba ben python ogreniyom")

####################
# Zip
####################

students = ["John", "Mark", "Venessa", "Mariam"]

departments =  ["mathematics", "statistics","physics","astronmy"]

ages = [ 23, 30, 26, 22]

list(zip(students,departments,ages))
#farklı listeleri listeler halinde tek bir listede birleştirir.

#################################
# lambda, map, filter, reduce
################################
def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a,b:a + b #kullan at fonksiyonlardır.

new_sum(4,5)

# map

salaries = [1000, 2000, 3000, 4000, 5000]
def new_salary(x):
    return x* 20/100+x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary,salaries)) #for döngüsü yazmadan üzerinde gezinebileceğin iterasyon ile aynı işlemi yapar.

# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))

# filter
list_stroe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, list_stroe)) #2'ye bölünenleri listeye alır.

# reduce
from functools import reduce
list_stroe =  [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_stroe)
####################################################
string = "abracadabra"
group = []

for index, letter in enumerate(string,1):# 1'in anlamı index'i 1'den başlat demek.
    if index * 2 % 2 == 0:
        group.append(letter)

print(group)

city_name = ["Londan", "Paris", "Berlin"]

def plate(cities):
    for index, city in enumerate(cities,1):
        print(f"{index} : {city}")
plate(city_name)

