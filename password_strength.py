import re


def get_password_strength(password):
    strength = 0
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[ !#$%&():*+,-./[\\\]^_`{|}~]', password):
        strength += 2
    if len(password) > 8:
        strength += 2
    if len(password) > 16:
        strength += 2
    if re.search(r'[\w][\d][\w][\d][\w][\d]', password):
        strength += 1
    return strength


if __name__ == '__main__':
    print('Проверка сложности пароля. 1 — очень слабый, 10 — хороший пароль')
    paswd = input('Введите пароль: ')
    print('Сложность вашего пароля: {}'.format(get_password_strength(paswd)))
