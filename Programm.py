import logging
from random import randint

# запускаем лог
logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.info('Statred')

# вводим размер
n = int(input("Введите n: "))

# создаем массив
nn = [ x+1 for x in range(n) ]

# перебираекм
while (len(nn) > 0):
    p = randint(0, len(nn)-1)
    
    # выбираем одно число
    s = "N=" + str(nn[p]) + " (from " + str(nn) + ")"
    logging.info( s )
    print( s )

    # удаляем его
    del nn[p]

    input("Нажмите enter, чтобы продолжить: ")

# конец
logging.info( "End" )
