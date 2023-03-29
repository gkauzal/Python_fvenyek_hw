# 1. feladat
def hwFirst(start, finish, divisible, not_divisible):
    nums = []
    x = range(start, finish + 1)
    for n in x:
        if n % divisible == 0 and n % not_divisible != 0:
            nums.append(n)
    return nums


print(hwFirst(2000, 3200, 7, 5))


#2. feladat
def hwSecond(name_list, f_name):
    counter = 0
    for name in name_list:
        if name == f_name:
            counter += 1
    return counter


print(
    hwSecond([
        'Pista', 'Gabor', 'Pista', 'Gábor', 'István', 'István', 'László',
        'Katalin', 'Katalin', 'Tímea', 'Gábor', 'Pista'
    ], 'Pista'))


#3. feladat
def convert_to_number(text):
    try:
        data = int(text)
        return data
    except ValueError:
        print("Invalid input")


def print_hello(count):
    try:
        if isinstance(count, int):
            i = 1
            while i < count + 1:
                print(str(i) + ".Hello")
                i += 1
    except ValueError:
        print("Invalid input")


print_hello(convert_to_number(input("Enter a Number: ")))

#4. feladat


def hwFourth(text):
    try:
        if isinstance(text, int):
            datas = []
            pi = 3.14
            datas.insert(0, 2 * pi * text)
            datas.insert(1, text * text * pi)
            return datas
    except ValueError:
        print("Invalid input")


print(hwFourth(convert_to_number(input("Enter a Number: "))))


#5. feladat
def hwFifth(name_list):
    sorted_name_list = sorted(name_list)
    count_nl = len(name_list)
    if count_nl % 2 == 0:
        print("1. csoport")
        i = 0
        while i < count_nl / 2:
            print(sorted_name_list[i])
            i += 1
        print("2.csoport")
        j = int(count_nl / 2)
        while j < count_nl:
            print(sorted_name_list[j])
            j += 1
    else:
        print("1. csoport")
        i = 0
        while i < (count_nl - 1) / 2:
            print(sorted_name_list[i])
            i += 1
        print("2.csoport")
        j = int(count_nl / 2)
        while j < count_nl:
            print(sorted_name_list[j])
            j += 1


hwFifth([
    'Gaál Bernadett', 'Szamosi Judit', 'Tóth Sára', 'Magyar Eszter',
    'Gaál András', 'Németh Diána', 'Telek Éva', 'Ledán-Munteán Szabolcs',
    'Mészáros Melinda', 'Lukács Dániel', 'Kucsera Bálint', 'Kovács Tamás'
])
