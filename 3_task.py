my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(my_favorite_movies)
# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.
my_favorite_movies.replace(',', '')
print(my_favorite_movies.replace(',', '')[0:10])
print(my_favorite_movies.replace(',', '')[38:53])
print(my_favorite_movies.replace(',', '')[11:25])
print(my_favorite_movies.replace(',', '')[32:37])