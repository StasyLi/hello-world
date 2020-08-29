from bottle import request, response, route, run
import json
@route ('/hello', method = 'OPTIONS')
def enableCORSGenericRoute():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token'
@route ('/hello', method = 'POST')
def hello():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token'
    import re
    a = request.json['vot']
    with open ('list.txt', 'a') as f:
        print(a, file = f)
        f.close()
    print(a, '0')
    digits = []
    letters = []
    sep = [-1, -1]
    m = [-1]
    sepa = []
    print(a, '48')
    sokr = ['тыс', 'млн', 'млрд', 'трлн']  # это не весь список чисел, его заполню ещё числами побольше
    more1 = ['десяток', 'дюжина', 'тысяча', 'миллион', 'миллиард', 'триллион'] # это не весь список чисел, его заполню ещё числами побольше
    more2 = ['десяток', 'десятка', 'десятков', 'тысяча', 'тысячи', 'тысяч', 'миллион', 'миллионов', 'миллиона', 'миллиард',
             'миллиарда', 'миллиардов', 'триллион', 'триллиона', 'триллионов']
    big_num = ['тысяча', 'тысячи', 'тысяч', 'миллион', 'миллионов', 'миллиона', 'миллиард',
             'миллиарда', 'миллиардов', 'триллион', 'триллиона', 'триллионов']
    ed = ['ноль', 'нуль', 'один', 'одна', 'два', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    des = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    nedodes = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать', 'восемнадцать', 'девятнадцать']
    sot = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    obsch = [more1,sot, des, nedodes, ed]
    seccheck = [big_num, sot, des, nedodes, ed]
    count = 0
    tcount = 0
    fcount = 0
    print(a)
    if len(a) > 30:
        print(a, '1')
        print('Лимит символов превышен')
        response.headers['Content-Type'] = 'application/json'
        return json.dumps({'result':'Лимит символов превышен'})
    elif len(a) == 0:
        print('Вы ничего не ввели. Это не число. 1')
        with open ('list.txt', 'a') as f:
            print(' Вы ничего не ввели', file = f)
            f.close()
        response.headers['Content-Type'] = 'application/json'
        return json.dumps({'result': 5})
    else:
        print(a)
        if a == r'[π|φ|(пи)|(pi)|G|e|c|h|k|r|f|(.+\!)]i{1}':
            print('Вы ввели "', a, '" . Это число. 1')
            response.headers['Content-Type'] = 'application/json'
            return json.dumps({'result': 1})
        else:
            print(a)
            lis = re.findall(r'\W^\.,', a)  # тут проверка по знакам
            if len(lis) > 1:
                print('Вы ввели "', a, '" . Это не число. 2')
                response.headers['Content-Type'] = 'application/json'
                return json.dumps({'result':0})
            else:
                print(a)
                print(4)
                a = re.sub(r'(\,|\/)', '.', a)
                try:
                    float(a)
                    print('Вы ввели "')
                    print(a)
                    print('" . Это число. 2')
                    response.headers['Content-Type'] = 'application/json'
                    return json.dumps({'result':1})
                except ValueError:  # тут пошла проверка 16-ричных чисел
                    print(a, '6')
                    lis = re.findall(r'[0-9A-F]{1}', a)
                    if len(a) - len(lis) == 0:
                        print('Вы ввели "', a, '" . Это число. 3')
                        response.headers['Content-Type'] = 'application/json'
                        return json.dumps({'result':1})    
                    else:
                        b = a.split()  # может, попоробовать причислить к действ.члены массива?
                        for x in b:
                            try:
                                float(x)
                                digits.append(x)
                            except ValueError:
                                print(a, '7')
                                letters.append(x)
                        if len(digits) != 0:
                            for x in letters:  # тут пошла проверка буквенных чисел сравниванием с членами созданных массивов
                              # если у нас смешанное число, то буквенные части могут быть только из списков sokr & more2
                                for z in sokr:
                                    for y in more2:
                                        if x != z and x != y:
                                            print(a, '8')
                                            print('Вы ввели "', a, '" . Это не число. 3')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':0})
                                        else:
                                            print(a, '9')
                                            print('Вы ввели "', a, '" . Это число. 4')  # этап проверки смешанных чисел закончился, дальше идёт этап проверки только буквенных чисел
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':1})
                        else:  # тут у нас только буквенные числа проверяются, если слово одно - проверяем по всем спискам.
                            if len(b) == 1:
                                print(a, '10')
                                for h in range(1):
                                    for x in obsch:
                                        for i in x:
                                            if i == b[0]:
                                                print(a, '11')
                                                print('Вы ввели "', a, '" . Это число. 5')# как тут сделать так, чтобы при совпадении программа остановилась?
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':1})
                                            elif obsch.index(x) == 4 and x.index(i) == 12:#это типа если мы проверили самое последнее число из списков и ничего не совпало, то всё, это точно не число
                                                print(a, '12')
                                                print('Вы ввели "', a, '" . Это не число. 4')
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':0})
                            elif len(b) == 0:
                                print('Вы ничего не ввели. 5')
                                response.headers['Content-Type'] = 'application/json'
                                return json.dumps({'result':'Вы ничего не ввели'})
                            else:#тут проверяем ввод больше, чем 1 слово
                                for i in b:
                                    for x in more2:
                                        if i == x:
                                            print(a, '13')
                                            count += 1
                                            sep[count-1] = b.index(i)  # покажет номер первого входа i в b
                                            sepa.append(x)#тут добавляем само слово-разделитель, чтобы потом посмотреть, не совпадают ли разделители
                                if len(sepa) > 0:
                                    for i in range (len(sepa)):
                                        if len(sepa) > 1 and sepa[i] == sepa[i+1]:
                                            print('Вы ввели "', a, '" . Это не число. 6')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':0})
                                    print(a, '13')
                                    nmax, nmin = count + 1, count - 1
                                    if nmin == -1:
                                         nmin = 1
                                    if sep[1] != -1:
                                        sep.append(2 * len(b))  # тут при отстутствии разделителей ошибка второй член списка = -1, нужно иф сюда
                                    else:
                                        sep[1] = 2 * len(b)
                                    if nmin <= (len(b) - count) <= nmax * 3:  # это мы проверили, правильное ли количество циклов "сотня-десяток-единица" присутствует в написанной строке

                                            # тут нужно найти промежутки (c помощью индексов разделителей в списке) перед первым разделителем, между ними и после последнего разделитедя и внутри них проводить поиск из общего списка
                                        for z in range(1, len(sep)):  # !!! было (len(sep) -1
                                            for i in range(sep[z-1] + 1, sep[z] - len(b)):  # это мы ввели переменные для определения участков поиска между разделителями в строке
                                                for g in obsch:  # теперь вводим списки, в которых ищем. Тут будет накладка - каждый раз будет проходить обыск сначала с большего списка, но это хорошо, т.к. поможет найти нечисло
                                                    for c in g:
                                                         if b[i] == c:
                                                               m.append(obsch.index(g))
                                                               try:
                                                                   if m[z] < m[z-1] or (m[z] == 2 and m[z - 1] == 1) or (m[z] == 3 and m[z - 1] == 2):  # то есть если индекс одного больше другого, то класс одного числа меньше предыдущего, что правильно для записанного числа, а два or - это и есть проверка проблем с недодесятками
                                                                       print('Вы ввели "', a, '" . Это не число. 7')
                                                                       fcount += 1
                                                                       response.headers['Content-Type'] = 'application/json'
                                                                       return json.dumps({'result':0})
                                                                   else:  # если всё хорошо, то всё опять начинается, но уже для другого слова из строки b
                                                                       break
                                                                   break
                                                               except IndexError:
                                                                   fcount += 1
                                                                   print('Вы ввели "', a, '" . Это не число. 8')
                                                                   response.headers['Content-Type'] = 'application/json'
                                                                   return json.dumps({'result':0})
                                                                   break
                                                               break
                                                         break
                                            m.clear()
                                            m = [-1]  # тоже нужно, чтобы с 1 разом не было непорядка
                                        if fcount == 0:
                                            print('Вы ввели "', a, '" . Это число. 30')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':1})
                                    else:  # если у нас не совпадают количество циклов возможное и реальное
                                        print(a, '15')
                                        print('Вы ввели "', a, '" . Это не число. 9')
                                        response.headers['Content-Type'] = 'application/json'
                                        return json.dumps({'result':0})
                                else:#тут нужно проверить, принадлежат ли числа к массивам + как-то сделать проверку порядка, в котором идут слова.
                                    for h in seccheck: # придумываем обозначения для разрядов, чтобы потом проверять расстояние между ними и их количество
                                        for s in b: #"тысячи" - 10. "миллион" - 11. они не могут повторяться в числе. сотни - 12. десятки - 13. недодесятки - 14. единицы - 15. они могут повторяться в числе, между ними должен быть разделитель. если его нет - не число
                                            if s != h:
                                                print('Вы ввели "', a, '" . Это не число. 10')
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':0})
                                    print('Вы ввели "', a, '" . Это число. 9')#то есть тут, если программа дошла до этого места, то всегда было s==h, значит введенные данные содержать слова из массивов с числами
                                    response.headers['Content-Type'] = 'application/json'
                                    return json.dumps({'result':1})
run(host='0.0.0.0', port = 8080, debug = True)                    


