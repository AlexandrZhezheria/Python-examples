# Згідно з міфами, Адам і Єва були першими людьми, які блукали по Землі.
# Ви повинні виконати Божу роботу.
# Фукція god повинна повертати список з довжиною 2, що містить об’єкти (що представляють Адама і Єву).
# Першим об’єктом у списку має бути екземпляр класу Man.
# Другий має бути екземпляром класу Woman.
# Обидва об’єкти мають бути підкласами Human.
# Ваше завдання — реалізувати класси «Human, Man і Woman».

class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def god() -> list:
    adam = Man()
    eve = Woman()
    return [adam, eve]