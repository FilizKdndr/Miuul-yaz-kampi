############################################################
# Görev 1: Verilerin değerlerin veri yapılarını inceleyiniz.
###########################################################

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

list = [x, y, z, a, b, c, l, d, t, s]

for i in list:
    list_type = type(i)
    print(list_type)

########################################################################
# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
#######################################################################

text = "The goal is to turn data into information, and information into insight"

text1 = text.upper().replace(","," ").replace("."," ").split()

##############################################################
# Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
##############################################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

#Adım 1: Verilen listenin eleman sayısına bakınız.
len(lst)
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]
lst[10]
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
new_lst = lst[0:4]
#Adım 4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)
#Adım 5: Yeni bir eleman ekleyiniz.
lst.append("S")
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8,"N")

##################################################################
# Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
#################################################################

dict = {'Christan': ["American",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",24]}

#Adım 1: Key değerlerine erişiniz.
dict.keys()
#Adım 2: Value'lara erişiniz.
dict.values()
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1] = 13
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({"Ahmet": ["Turkey", 24]})
#Adım 5: Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")

#####################################################################
# Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve
# çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.
#####################################################################

l = [2, 13, 8, 93, 22]
even_list = []
odd_list = []
def func(l):
    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list

even_list, odd_list = func(l)
print(even_list)
print(odd_list)

#####################################################################################################################
# Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
#####################################################################################################################

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenciler in enumerate(ogrenciler,1):
    if index < 4:
        print("Mühendislik Fakültesi", index,". öğrenci:", ogrenciler)
    else:
        print(f"Tıp Fakültesi {index -3}. öğrenci: {ogrenciler}")

##############################################################################
# Görev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin
# kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################################################

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150,25]



