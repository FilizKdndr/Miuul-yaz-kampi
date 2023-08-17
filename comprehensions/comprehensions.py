############################################
# Comprehensions
############################################

##########################
# List Comprehension
#########################

salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    if salary >  3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000 ] #if yapısını tek başına kullanıyorsak if yapısı en sağda olur.

[salary * 2  if salary < 3000 else salary * 0 for salary in salaries] #if else şeklinde kullanacakcak for yapısı en sağda olur.

[new_salary(salary * 2)  if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]


students =  ["John", "Mark", "Venessa", "Maram"]

students_no =  ["John", "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

[student.upper() if student not in students_no else student.lower() for student in students]

##########################
# Dict Comprehension
##########################

dictionary =  { 'a': 1,
                'b': 2,
                'c': 3,
                'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v  for (k, v) in dictionary.items()}

{k.upper(): v*2  for (k, v) in dictionary.items()}

############################
# Uygulama- Mülakat Sorusu
############################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir
# Keyler orjinal değerler valueler ise değiştirilmiş değerler olacaktır.

numbers =  range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2 # key kısmına n ekledik value kısmına n^2'i eklenmiş oldu.

{n: n ** 2 for n in numbers if n % 2 == 0}

#############################################
# List & Dict COmprehension Uygulamalar
############################################

# Bir Veri Setindeki değişken isimlerini değiştirmek

# before:
# [ 'total', 'speeding', 'alcohol', 'not_dictracted', 'no_previous', 'ins_premium', 'ins_loses', 'abbrev']
# after
# [ 'TOTAL', 'SPEADING', 'ALCOHOL', 'NOT_DICTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSES', 'ABBREV']
#dataframe pandas kütüphanesinin veri yapısıdır, birbirinden farklı tiplerdeki verileri tutmayı sağlar.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

A = []

for col in df.columns:
    A.append(col.upper())

df.columns =  A

df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz

# before:
# [ 'TOTAL', 'SPEADING', 'ALCOHOL', 'NOT_DICTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSES', 'ABBREV']
# after:
# [ 'NO_FLAG_TOTAL', 'NO_FLAG_SPEADING', 'NO_FLAG_ALCOHOL', 'NO_FLAG_NOT_DICTRACTED', 'NO_FLAG_NO_PREVIOUS', 'FLAG_INS_PREMIUM', 'FLAG_INS_LOSES', 'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]

["FLAG_"+ col for col in df.columns if "INS" in col]

["FLAG_"+ col  if "INS" in col else "NO_FLAG_"+ col for col in df.columns]

df.columns = ["FLAG_"+ col  if "INS" in col else "NO_FLAG_"+ col for col in df.columns]

# Amaç key'i string , valuesi aşağıdaki gibi bir liste olan sözlük oluşturmak
# Bu işlemi sadece sayısal değişkenler için yapmak istiyoruz

# Output:
# { 'total':['mean','min', 'max', 'var'] ,
# 'speeding':['mean','min', 'max', 'var'] ,
# 'alcohol':['mean','min', 'max', 'var'] ,
# 'not_dictracted':['mean','min', 'max', 'var'] ,
# 'no_previous':['mean','min', 'max', 'var'] ,
# 'ins_premium':['mean','min', 'max', 'var'] ,
# 'ins_loses':['mean','min', 'max', 'var'] }

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols =  [col for col in df.columns if df[col].dtype != "O"] #"O" object anlamına gelir. burada object olmayanı arıyoruz yani numerik tiptekileri.
soz = {}
agg_list =  ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] =  agg_list

#kısa yol

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)

wages = [1000,2000,3000,4000,5000]
new_wages =  lambda  x: x*0.20+x
list(map(new_wages,wages))

students = ["Denise", "Arsem","Tony","Audrey"]
low =  lambda x: x[0].lower()
print(list(map(low,students)))

dictn = {"Denise": 10, "Arsen": 12, "Tony": 15, "Audrey": 17}
new_dict =  {k: v*2 + 3 for (k, v) in dictn.items()}
new_dict

numbers = range(1,10)
numsda = {n: n ** 2 for n in numbers if n %2 != 0}