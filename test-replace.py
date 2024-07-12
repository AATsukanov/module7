SYMBOLS_TO_REPLACE = ['ъ', ',', '.', '=', '!', '?', ';', ':', ' - ']

line = 'Вася и Пётръ, пошли гулять в лес?'

for s in SYMBOLS_TO_REPLACE:
    line = line.replace(s, '')
print(line)