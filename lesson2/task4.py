# Fourth task

words = str(input('Ведите любое предложение:'))

number_of_words = 0
for k in words.split(' '):
    number_of_words += 1
    print(str(number_of_words) + ':' + k[0:10])
