from bottle import route, run, request, response
import json
@route ('/hello', method = "OPTIONS")
def enableCORSGenericRoute():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token' 
    print(request.headers.get('Content-Type'))
@route ('/hello', method='POST')
def hello(): #xmlhttp.onreadystatechange
    import re
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token' 
    response.headers['Content-Type'] = 'json'
    a = request.json['vot']
    print(a)
    digits = []
    letters = []
    sep = [-1, -1]
    m = [-1]
    sepa = []
    sokr = ['тыс', 'млн', 'млрд', 'трлн']  # это не весь список чисел, его заполню ещё числами побольше
    more1 = ['десяток', 'дюжина', 'тысяча', 'миллион', 'миллиард', 'триллион']
    more2 = ['десяток', 'десятка', 'десятков', 'тысяча', 'тысячи', 'тысяч', 'миллион', 'миллионов', 'миллиона', 'миллиард',
             'миллиарда', 'миллиардов', 'триллион', 'триллиона', 'триллионов']
    ed = ['ноль', 'нуль', 'один', 'одна', 'два', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    des = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    nedodes = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
               'семнадцать', 'восемнадцать', 'девятнадцать']
    sot = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    obsch = [more1,sot, des, nedodes, ed]
    count = 0
    if len(a) > 30:
        print('Лимит символов превышен')
        response.headers['Content-Type'] = 'application/json'
        return json.dumps({'result':'Лимит символов превышен'})
    elif len(a) == 0:
        print('Вы ничего не ввыели. Это не число. 0')
        response.headers['Content-Type'] = 'application/json'
        return json.dumps({'result': 0})
    else:
        if a == r'[π|φ|(пи)|(pi)|G|e|c|h|k|r|f|(.+\!)]i{1}':
            print('Вы ввели "', a, '" . Это число.')
            response.headers['Content-Type'] = 'application/json'
            return json.dumps({'result': 1})
        else:
            lis = re.findall(r'\W^\.,', a)  # тут проверка по знакам
            if len(lis) > 1:
                print('Вы ввели "', a, '" . Это не число. 1')
                return json.dumps({'result':0})
            else:
                a = re.sub(r'(\,|\/)', '.', a)
                try:
                    float(a)
                    print('Вы ввели "', a, '" . Это число.')
                    response.headers['Content-Type'] = 'application/json'
                    return json.dumps({'result':1})
                except ValueError:  # тут пошла проверка 16-ричных чисел
                    lis = re.findall(r'[0-9A-F]{1}', a)
                    if len(a) - len(lis) == 0:
                        print('Вы ввели "', a, '" . Это число.')
                        response.headers['Content-Type'] = 'application/json'
                        return json.dumps({'result':1})                     # и тут надо закончить выполнение программы (а оно и закончится)
                    else:  # тут пошла проверка смешанных чисел
                        b = a.split()  # может, попоробовать причислить к действ.члены массива?
                        for x in b:
                            try:
                                float(x)
                                digits.append(x)
                            except ValueError:
                                letters.append(x)
                        if len(digits) != 0:
                            for x in letters:  # тут пошла проверка буквенных чисел сравниванием с членами созданных массивов
                              # если у нас смешанное число, то буквенные части могут быть только из списков sokr & more2
                                for z in sokr:
                                    for y in more2:
                                        if x != z and x != y:
                                            print('Вы ввели "', a, '" . Это не число. 2')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':0})
                                        else:
                                            print('Вы ввели "', a, '" . Это число.')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':1})  # этап проверки смешанных чисел закончился, дальше идёт этап проверки только буквенных чисел
                        else:  # тут у нас только буквенные числа проверяются, если слово одно - проверяем по всем спискам.
                                if len(b) == 1:
                                    print('Это b[0] - ', b[0])
                                    for h in range(1):
                                        for x in obsch:
                                            for i in x:
                                                if i == b[0]:
                                                    print('Вы ввели "', a, '" . Это число.')
                                                    response.headers['Content-Type'] = 'application/json'
                                                    return json.dumps({'result':1})# как тут сделать так, чтобы при совпадении программа остановилась?
                                                    break
                                                elif obsch.index(x) == 4 and x.index(i) == 12:#это типа если мы проверили самое последнее число из списков и ничего не совпало, то всё, это точно не число
                                                    print('Вы ввели "', a, '" . Это не число. 3')
                                                    response.headers['Content-Type'] = 'application/json'
                                                    return json.dumps({'result':0})
                                                    break
                                elif len(b) == 0:
                                    print('Вы ввели "', a, '" . Это не число. 4')
                                    response.headers['Content-Type'] = 'application/json'
                                    return json.dumps({'result':0})
                                else:
                                    for i in b:
                                        for x in more2:
                                            if i == x:
                                                count += 1
                                                sep[count-1] = b.index(i)  # покажет номер первого входа i в b
                                                sepa.append(x)#тут добавляем само слово-разделитель, чтобы потом посмотреть, несовпадают ли разделители
                                    for i in range (len(sepa)):
                                        if len(sepa) > 1 and sepa[i] == sepa[i+1]:
                                            print('Вы ввели "', a, '" . Это не число. 5')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':0})
                                            break
                                        break## тут всё равно до конца выход из программы не совершается
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
                                                                       print('Вы ввели "', a, '" . Это не число. 6')
                                                                       response.headers['Content-Type'] = 'application/json'
                                                                       return json.dumps({'result':0})
                                                                   else:  # если всё хорошо, то всё опять начинается, но уже для другого слова из строки b
                                                                       break
                                                                   break 
                                                               except IndexError:
                                                                   print('Вы ввели "', a, '" . Это не число. 7')
                                                                   response.headers['Content-Type'] = 'application/json'
                                                                   return json.dumps({'result':0})
                                                                   break
                                                               break
                                                         break
                                            m = m.clear()
                                            m = [-1]  # тоже нужно, чтобы с 1 разом не было непорядка
                                        print('Вы ввели "', a, '" . Это число.')
                                        response.headers['Content-Type'] = 'application/json'
                                        return json.dumps({'result':1})
                                        # нужно исключить случай, когда в (недодес и ед) или (дес и недодес) есть числа. То есть где-то только в одном месте они моугт быть, иначе - не число
                                    else:  # если у нас не совпадают количество циклов возможное и реальное
                                        print('Вы ввели "', a, '" . Это не число. 8')
                                        response.headers['Content-Type'] = 'application/json'
                                        return json.dumps({'result':0})
run(host='localhost', port=8080, debug=True)
