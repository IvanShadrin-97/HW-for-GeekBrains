import time


'''
До начала прохождения курса GeekBrains прошёл краткий интерактивынй курс на letpy.com. 
Так что буду стараться решать задания максимально компактными способами.
'''


#First task
var = 1
second_var = 2
third_var = 196
var_str = 'Hello firs Home Work;)'
user_input_int =int(input('Ведите число'))
user_input_str =str(input('Ведите текст'))

print(var, second_var, third_var, var_str, user_input_int, user_input_str)

#Second task

t = int(input('Ведите количество секунд:'))
convert_sec_to_time = time.strftime('%H:%M:%S', time.gmtime(t))
print('Конвертация секунд прошла успешно:' + convert_sec_to_time)

#Third task

def tripelplus(n):
    x = int(n)
    y = int(n + n)
    z = int(n + n + n)
    return x + y + z

while True:
    try:
        print(tripelplus(input('Ведите число:')))
        print('Выполнилось вычеслние x + xx + xxx')
        break
    except:
        print('Убедитесь что вы велли число')

#Fourth task

x = input('Ведите число:')
y = 0
for i in str(x):
    i = int(i)
if i > y:
    y = i
    print(i)

'''P.S это превое что пришлов  голову при при решение даного задния с циклом while сам ничего не смог придумать
подсмотрел в интрнете и это оказлось очень запутно к такой логике я сам прийти не смог.
i = input()
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r) 

'''

#Fifth task В этой задаче очень сильно хотелось написать ещё раз команду if result > 0:, но потом в голву приходит DRY)

profit = int(input('Какова выручка вашей фирмы:'))
spending = int(input('Каковы издрежки вашей фирмы:'))
result = profit - spending

if result > 0:
    print('Ваша выручка больше ваших издержок')
    print('Ваша рентабильность составила ' + str(result / profit * 100) + '%')
    personal = int(input('Ведите количство ваших сотрудников: '))
    print('Прибыль вашей фирмы на одного сотрудника состовляет: ' + str(result / personal))
elif result == 0:
    print('Вы работете в ноль')
else:
    print('Ваши издержки привышают вашу прибыль')

#Sixth task

def run_target(a, b):
    i = 1
    print('1-й день:' + str(a))
    while a < b:
        i += 1
        a = a + (a * 0.1)
        print(str(i) + '-й день:' + str(a))
    return print('На ' + str(i) + '-й день вы достигните результата отметкой ' + str(b) )

'''В данном задние хорошо-бы ещё убрать до 2-ого знака после запятой,  но при использовании метода {%.2f}(a) у меня н
у меня не получиль правильно произвести конкатенацию. Всё время происходит ошибка с str или int.
'''
print(run_target(2,3))

