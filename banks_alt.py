#процентная ставка
t = 5.6#ТКБ
c = 5.9#СКБ
v = 4.28#ВТБ
cb = 4#СБЕР
print('Процентные ставки банков:', "\n ТКБ", t, '%', '\n СКБ', c, "%", "\n ВТБ", v, '%', '\nСБЕР', cb, '%')
a = float(input("Введите сумму депозита: "))
print(" ТКБ", round(a*t/100, 2), '\n', "СКБ", round(a*c/100, 2), '\n', "ВТБ", round(a*v/100, 2), '\n' "СБЕР", round(a*cb/100, 2))
print('Самая большая сумма:', round(max(t*a/100, c*a/100, v*a/100, cb*a/100), 2))