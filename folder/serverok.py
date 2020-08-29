from bottle import request, response, route, run
import json
@route ('/hello', method = 'OPTIONS')      #actually there are 2 requests, and the first one is OPTIONS request
def enableCORSGenericRoute():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token'
@route ('/hello', method = 'POST')     #the second request is the one we've been working on during forming ajax-request in index.html 
def hello():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET, POST'
    response.headers['Access-Control-Max-Age'] = 1000
    response.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept, x-csrf-token'
    import re
    a = request.json['vot']
    with open ('list.txt', 'a') as f: #here is the interaction of list.txt and this program
        print(a, file = f)
        f.close()
    print(a, '0')                 #these prints will appear - we need them for debugging
    digits = []
    letters = []
    sep = [-1, -1]
    m = [-1]
    sepa = []
    print(a, '48')
    sokr = ['тыс', 'млн', 'млрд', 'трлн']     #ok, it's kind of too short)
    more1 = ['десяток', 'дюжина', 'тысяча', 'миллион', 'миллиард', 'триллион'] 
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
        if a == r'[π|φ|(пи)|(pi)|G|e|c|h|k|r|f|(.+\!)]i{1}':        #there are some constants used in physics and maths
            print('Вы ввели "', a, '" . Это число. 1')
            response.headers['Content-Type'] = 'application/json'
            return json.dumps({'result': 1})
        else:
            print(a)
            lis = re.findall(r'\W^\.,', a)         #here we check if there are any signs which usually don't present in numbers
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
                except ValueError:            #here we check if the data is a hexadecimal number
                    print(a, '6')
                    lis = re.findall(r'[0-9A-F]{1}', a)
                    if len(a) - len(lis) == 0:        #if there are no symbols except the parts of hexadecimal number, it's a hexadecimal number (rather obviously))
                        print('Вы ввели "', a, '" . Это число. 3')
                        response.headers['Content-Type'] = 'application/json'
                        return json.dumps({'result':1})    
                    else:
                        b = a.split()
                        for x in b:
                            try:
                                float(x)
                                digits.append(x)
                            except ValueError:
                                print(a, '7')
                                letters.append(x)
                        if len(digits) != 0:
                            for x in letters:          #here we check the match between the data and alphabetic numbers from our own lists 
                                                       #if the data is a mixed number, alphabetic parts can only belong to sokr & more2 lists
                                for z in sokr:
                                    for y in more2:
                                        if x != z and x != y:
                                            print(a, '8')
                                            print('Вы ввели "', a, '" . Это не число. 3')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':0})
                                        else:
                                            print(a, '9')
                                            print('Вы ввели "', a, '" . Это число. 4')     #the stage of checking mixed numbers is over. Further we'll check if the data is a completely alphabetical number
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':1})
                        else:       # here we check if the data is a completely alphabetical number. If there is only 1 word, we compare it to every member of every list
                            if len(b) == 1:
                                print(a, '10')
                                for h in range(1):
                                    for x in obsch:
                                        for i in x:
                                            if i == b[0]:
                                                print(a, '11')
                                                print('Вы ввели "', a, '" . Это число. 5')       # when I ran this program as a common programm, not as a server, I couldn't terminate it using "break"s. 
                                                                                                 #Command "sys.exit() really helped me out. If you use it, do "import sys" at first
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':1})
                                            elif obsch.index(x) == 4 and x.index(i) == 12:     #if all of the members of all the lists didn't coincide with the data, the data is surely not a number 
                                                print(a, '12')
                                                print('Вы ввели "', a, '" . Это не число. 4')
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':0})
                            elif len(b) == 0:
                                print('Вы ничего не ввели. 5')
                                response.headers['Content-Type'] = 'application/json'
                                return json.dumps({'result':'Вы ничего не ввели'})
                            else:           #here we check the data which has more than one word
                                for i in b:
                                    for x in more2:
                                        if i == x:
                                            print(a, '13')
                                            count += 1
                                            sep[count-1] = b.index(i) 
                                            sepa.append(x)      #here we add the word-separator to list 'sepa' to check later if separators coincide with each other 
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
                                        sep.append(2 * len(b))
                                    else:
                                        sep[1] = 2 * len(b)
                                    if nmin <= (len(b) - count) <= nmax * 3:     # here we check if the quantity of "hundred-decade-unit" chain is correct in the data
                                    #with the help of separators' indexes in "sepa" we need to find out intervals before the first separator, between the separators and after final separator. 
                                    #Between these intervals we'll search for match between data words and members of our lists included in "obsch" list
                                        for z in range(1, len(sep)):  # !!! было (len(sep) -1
                                            for i in range(sep[z-1] + 1, sep[z] - len(b)):  # here are the variables for defining the intervals mentioned before
                                                for g in obsch:      # here we specify lists where the search is held
                                                    for c in g:
                                                         if b[i] == c:
                                                               m.append(obsch.index(g))
                                                               try:
                                                                   if m[z] < m[z-1] or (m[z] == 2 and m[z - 1] == 1) or (m[z] == 3 and m[z - 1] == 2):  # so if one index is bigger than another one, the class of the first number is under the class of another number. It's correct for alphabetic numbers.  
                                                                       print('Вы ввели "', a, '" . Это не число. 7')
                                                                       fcount += 1
                                                                       response.headers['Content-Type'] = 'application/json'
                                                                       return json.dumps({'result':0})
                                                                   else:     #if everything is OK, we redo this part of code for another member of the string "b" 
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
                                            m = [-1]  # we need it to not to have problems with the first launch
                                        if fcount == 0:
                                            print('Вы ввели "', a, '" . Это число. 30')
                                            response.headers['Content-Type'] = 'application/json'
                                            return json.dumps({'result':1})
                                    else:  # here are the steps needed in case if the real and correct quantities of "hundred-decade-unit" chains don't coincide with each other
                                        print(a, '15')
                                        print('Вы ввели "', a, '" . Это не число. 9')
                                        response.headers['Content-Type'] = 'application/json'
                                        return json.dumps({'result':0})
                                else:     #here we check if words from string 'b' coincide with the members of our own lists
                                    for h in seccheck: 
                                        for s in b: 
                                            if s != h:
                                                print('Вы ввели "', a, '" . Это не число. 10')
                                                response.headers['Content-Type'] = 'application/json'
                                                return json.dumps({'result':0})
                                    print('Вы ввели "', a, '" . Это число. 9')    # if the programm reached this part of code, then it was always s==h. It means the data includes members of our own lists
                                    response.headers['Content-Type'] = 'application/json'
                                    return json.dumps({'result':1})
run(host='0.0.0.0', port = 8080, debug = True)                    


