#ИСПОЛЬЗОВАТЬ ВНЕ КЛАССА РЕКОМЕНДУЕТСЯ ТОЛЬКО МЕТОДЫ, ПОМЕЧЕННЫЕ КАК ПУБЛИЧНЫЕ:
#НЕ ИМЕЮЩИЕ ПОДЧЁРКИВАНИЙ С ДВУХ СТОРОН.

def __P__(value = 0):
    if (value != 0):
        __P__.value = value
    return __P__.value
__P__.value = 0

def __Y__(value = 0):
    if (value != 0):
        __Y__.value = value
    return __Y__.value
__Y__.value = 0
#ВОЗВРАЩАЕТ ПАРУ ПРОИНИЦИАЛИЗИРОВАННЫХ ОБЪЕКТОВ,
#УСТАНАВЛИВАЕТ P И Y
def init_pair (A, B, P = __P__(), Y = __Y__()):
    __P__(P)
    __Y__(Y)
    first = person(A)
    second = person(B)
    return first, second

#ВЫВОДИТ НА ЭКРАН ОСНОВНЫЕ ЧИСЛА: P, Y, A И B
def print_situation (first, second):
    print ('P = ', __P__())
    print ('Y = ', __Y__())
    print ('A = ', end = '')
    first.__print__()
    print ('B = ', end = '')
    second.__print__()
    return 0

class person:
    def __init__ (self, SECRET):
        self.__secret__ = SECRET

    #ВОЗВРАЩАЕТ ЗНАЧЕНИЕ, КОТОРОЕ БУДЕТ ОТПРАВЛЕНО СОБЕСЕДНИКУ (a ИЛИ b)
    def get_msg(self):
        return __Y__() ** self.__secret__ % __P__()

    #ВОЗВРАЩАЕТ КЛЮЧ, СГЕНЕРИРОВАННЫЙ ОТ ПОЛУЧЕННОГО СООБЩЕНИЯ
    def get_key(self, msg):
        return msg ** self.__secret__ % __P__()

    #ПЕЧАТАЕТ _КАК-БЫ ПРИВАТНОЕ_ ПОЛЕ КЛАССА -- СЕКРЕТНОЕ ЧИСЛО 
    def __print__ (self):
        print (self.__secret__)
        return self
