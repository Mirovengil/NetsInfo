from random import *
import hashlib
from numba import jit #Это были _жалкие попытки_ разогнать python до сколько-нибудь приемлимой скорости. 
#В файле RANDOM.txt записаны простые числа до 3194159 (вы можете заполнить его любым способом -- не имеет значения, главное -- чтобы соблюдался формат файла,
#его имя и формат его содержимого: каждое число должно быть на отдельной строчке, никаких запятых -- только конец строки '\n'). Я заполнял их через СИ-шную программму,
#но она была утеряна. Если вам вдруг не хватит первых 230 000 простых чисел, которые уже есть в файле...

@jit
def get_simple_number(index = 0):
    return get_simple_number.value[index]
get_simple_number.value = []
file = open('./RANDOM.txt', 'r')
for i in file:
    get_simple_number.value.append(int(i))
file.close()

@jit
def find_in_mass(mass, value):
    i = 0
    while mass[i] > value:
        i = i + 1
    i = i - randint(1, 10)
    return mass[i]

@jit
def str_to_int (string):
    int_mass = []
    for i in string:
        int_mass.append(ord(i))
    return int_mass

@jit
def int_to_str(value):
    string = ""
    for i in value:
        string = string + chr(i)
    return string

class Object:
    @jit
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
    @jit
    def code_to(self, msg, other):
        i = 0
        while i < len(msg):
            msg[i] = pow(msg[i], other.__e__, other.__n__)
            i = i + 1
        return msg

    @jit
    def decode(self, msg):
        i = 0
        while i < len(msg):
            msg[i] = pow(msg[i], self.__d__, self.__n__)
            i = i + 1
        return msg

    @jit
    def set_signature(self, _hash):
        return pow(self.__make_hash__(_hash), self.__d__, self.__n__)

    @jit
    def chech_that_signature_is_of(self, signature, other):
        return pow(signature, other.__e__, other.__n__)

    @jit
    def __make_hash__(self, msg):
        return int(hashlib.md5(msg.encode()).hexdigest(), 16)
        
        

#ВАЖНО: К ЭТОЙ ФУНКЦИИ НЕЛЬЗЯ ПРИПИСЫВАТЬ "@git": ОНА ПЕРЕСТАЁТ РАБОТАТЬ!
def test_object(_object):
    for i in range(10):
        if (pow(pow(i, _object.__e__, _object.__n__), _object.__d__, _object.__n__) != i):
            return False
    return True

#ВАЖНО: К ЭТОЙ ФУНКЦИИ НЕЛЬЗЯ ПРИПИСЫВАТЬ "@git": ОНА ПЕРЕСТАЁТ РАБОТАТЬ!
#Благодаря сей функции вероятность ошибки снижена (проверил экспериментальным путём) до нуля (0/1000), правда, ценой некоторого увеличения времени работы.
def generate_object():
    rez = Object()
    while not test_object(rez):
        rez = Object()
    return rez
    
