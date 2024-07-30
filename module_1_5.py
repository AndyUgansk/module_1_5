immutable_var = 1, 2, 3, 4, True, "строка"
print(immutable_var, type(immutable_var))
#  immutable_var[0] = 20 # в этой строке появляется ошибка: 'tuple' object does not support item assignment
#  'Кортеж'. объект не поддерживает назначение элементов
mutable_list = [1, 2, 'a', 'b', 'UnModified']
print(mutable_list, type(mutable_list))
mutable_list[0] = 3
mutable_list[1] = 4
mutable_list[3] = 'c'
mutable_list[4] = 'Modified'
print(mutable_list)