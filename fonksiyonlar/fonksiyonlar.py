###########################################
# Fonksiyonlar ( Functions)
###########################################

# Fonksiyon Okuryazarlığı

print("a", "b")

print("a", "b", sep="--")

help(print) #fonksiyon hakkında bilgi almak

############################################
# Fonksiyon Tanımlama
############################################

def calculate(x):
    print(x*2)


calculate(5)


# İki argümanlı/ parametreli bir fonksiyon tanımlayalım

    def summer(arg1, arg2):
        """
        :param arg1: int, float
        :param arg2: int, float
        :return: int, float
        """

        print(arg1+arg2)

summer(5,6)

help(summer)

########################################
#Fonksiyonların Statement/ Body Bölümü
########################################

# def function_name(parameters/arguments):
#       statements ( function body)


def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")

say_hi()

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("Filiz")


def multiplication(a, b):
    c =  a * b
    print(c)

multiplication(10,9)


# girilen deerleri bir liste içinde saklayan fonksiyon

list_stroe = []

def add_element(a,b):
    c =  a * b
    list_stroe.append(c)
    print(list_stroe)

add_element(1,5)
add_element(18,8)
add_element(180,10)

########################################################
# Ön Tanımlı Argümanlar/ Parametreler ( Default Parameters / Arguments)
########################################################
def divide(a,b):
    print(a/b)


divide(1,2)

def divide(a,b=1):
    print(a/b)

divide(1)

def say_hi(string="Merhaba"):
    print((string))
    print("Hi")
    print("Hello")

say_hi()

#############################################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#############################################

#v varm, mousture, charge
def calculate(varm, moisture, charge):
    print((varm+moisture)/charge)

calculate(98,12,78)

#######################################################
# Return: Fonksiyon Çıktılarını Girdi olarak kullanmak
#######################################################

def calculate(varm, moisture, charge):
    return (varm+moisture)/charge

a1 = calculate(98,12,78)
a1
a2 = calculate(98,12,78)*10
a2

def calculate(varm, moisture, charge):
    varm = varm*2
    moisture = moisture*2
    charge = charge*2
    output = (varm+moisture)/charge
    return varm, moisture, charge, output

type(calculate(98,12,78))

charge: int | Any
varm, moisture, charge, output = calculate(98,12,78)

###############################################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
##############################################
 def calculate( varm, moisture, charge):
    return int((varm+moisture)/charge)

 calculate(90,12,12)*10

 def  standardization ( a, p):
     return  a * 10 / 100 * p * p

 standardization(45, 1)


 def all_calculation(varm, moisture, charge, p):
     a = calculate(varm,moisture,charge)
     b = standardization(a, p)
     print(b *10)

all_calculation(1, 3, 5, 12)

######################################
# Lokal & Global Değişkenler ( Local & Global Variables
#####################################

list_stroe = [1, 2]

def add_element(a, b):
    c = a * b
    list_stroe.append(c)
    print(list_stroe)

add_element(1,5)

