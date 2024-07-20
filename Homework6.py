print('Упражнение 1 "Работа со словарями":')
my_dict = {"Misha": 2002, "Dasha": 1997, "Roma": 2006}
print('Dict:', my_dict)
print('Existing value:', my_dict["Roma"], ', Not existing value:', my_dict.get("Anton"))
my_dict.update({'Oleg': 2000, 'Julia': 1995})
a = my_dict.pop('Misha')
print('Deleted value:', a)
print('Modified set:', my_dict)

print('Упражнение 2 "Работа с множествами":')
my_set = {77, 5, 0, 7, 5, 'World', 77, False, True, True}
print('Set:', my_set)
my_set.update([777, 111], ['Hello'])
my_set.remove(0)
print('Modified set:', my_set)
