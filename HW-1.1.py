#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.




seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
ostatok = seconds % 3600
minutes = ostatok // 60
sec = ostatok % 60
print("Ваше время {}:{}:{} ".format(hours, minutes, sec))