#Домашняя работа по уроку "Пространство имён"
#Задача "Счётчик вызовов"


def count_calls(с):
    global calls
    calls += с
    return calls

def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a


def is_contains(string_info, list_to_search):
    string_info.lower()
    new_list_to_search = []
    count_calls(1)
    for i in list_to_search:
        new_list_to_search.append(i.lower())
    return (string_info.lower() in new_list_to_search)


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

