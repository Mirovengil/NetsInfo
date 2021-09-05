from random import *
import hashlib

#В файле RANDOM.txt записаны простые числа до 3194159 (вы можете заполнить его любым способом -- не имеет значения, главное -- чтобы соблюдался формат файла,
#его имя и формат его содержимого: каждое число должно быть на отдельной строчке, никаких запятых -- только конец строки '\n'). Я заполнял их через СИ-шную программму,
#но она была утеряна. Если вам вдруг не хватит первых 230 000 простых чисел, которые уже есть в файле...
def get_simple_number(index = 0):
    return get_simple_number.value[index]
get_simple_number.value = []
file = open('./RANDOM.txt', 'r')
for i in file:
    get_simple_number.value.append(int(i))
file.close()

#Ищет первый элемент, больший искомого, а потом делает откат на несколько элементов назад.
def find_in_mass(mass, value):
    i = 0
    while mass[i] > value:
        i = i + 1
    i = i - randint(1, 10)
    return mass[i]

#Переводит строку в массив целых чисел
def str_to_int (string):
    int_mass = []
    for i in string:
        int_mass.append(ord(i))
    return int_mass

#Переводит массив целых чисел в строку
def int_to_str(value):
    string = ""
    for i in value:
        string = string + chr(i)
    return string


class Object:
    def __init__(self):
        max_len = 10000
        p = get_simple_number.value[randint(10, max_len)]
        q = get_simple_number.value[randint(10, max_len)]
        while p == q:
            q = randint(10, max_len)
        self.__n__ = p * q
        F_n = (p - 1) * (q - 1)
        self.__e__ = find_in_mass(get_simple_number.value, F_n)
        i = 1
        while not ((F_n * i + 1) / self.__e__).is_integer():
            i = i + 1
        self.__d__ = int((F_n * i + 1) / self.__e__)
        #При проведении тестов выяснилось, что хотя такой способ (сам придумал) нахождения d ускоряет алгоритм с ~минуты до ~трёх секунд, но существует верятность
        #ошибки, которая равна 28/1000, поэтому на всякий пожарный случай проводится проверка, будет ли работать сгенерированный объект.

    def code_to(self, msg, other): #Шифрует массив для пользователя other
        msg_ = msg.copy()
        i = 0
        while i < len(msg_):
            msg_[i] = pow(msg_[i], other.__e__, other.__n__)
            i = i + 1
        return msg_

    def decode(self, msg): #Вскрывает массив
        msg_ = msg.copy()
        i = 0
        while i < len(msg_):
            msg_[i] = pow(msg_[i], self.__d__, self.__n__)
            i = i + 1
        return msg_

    def set_signature(self, msg): #Возвращает вашу электронную подпись сего письма
        str_hash = self.__make_hash__(msg)
        int_hash = []
        i = 0
        while i < 16:
            int_hash.append(int(str_hash[i * 2: (i + 1) * 2], 16))
            i += 1
        i = 0
        while i < len(int_hash):
            int_hash[i] = pow(int_hash[i], self.__d__, self.__n__)
            i += 1
        return int_hash

    def check_that_signature_is_of(self, signature, other): #Вскрывает подпись, которая, как _предполагается_, принадлежит пользователю other
        i = 0
        copy = signature.copy()
        while i < len(copy):
            copy[i] = pow(copy[i], other.__e__, other.__n__)
            i = i + 1
        str_signature = ""
        for i in copy:
            str_signature += (str(hex(i)))[2:4]
        return str_signature 

    def __make_hash__(self, msg):
        return hashlib.md5(msg.encode()).hexdigest() #
        
        

def test_object(_object): #Проверяет, годен ли новосозданный объект
    for i in range(10):
        if (pow(pow(i, _object.__e__, _object.__n__), _object.__d__, _object.__n__) != i):
            return False
    return True

#Благодаря сей функции вероятность ошибки снижена (проверил экспериментальным путём) до нуля (0/1000), правда, ценой некоторого увеличения времени работы.
def generate_object():
    rez = Object()
    while not test_object(rez):
        rez = Object()
    return rez
    
