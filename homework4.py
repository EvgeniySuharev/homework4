immutable_var = ([1, 3, 5], 2.4, 'string', True)
print(immutable_var)
# immutable_var[1] = 2.6 - выдает ошибку, так как нельзя изменять элементы кортежа
mutable_list = ['pi', '=', 3.15]
mutable_list[2] = 3.14
print(mutable_list)
