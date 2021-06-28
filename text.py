import datetime

phrases = {
    'on_ready': 'я не сплю',
    'cutie_debug': 'random ganich',
    'join_connect': 'Ну-ка вышли все отсюда. Я щас полицию вызову',
    'join_another': 'Пздец за вами еще бегать блть. Где моё такси, сука?',
    'leave': 'Влад, вызывай мне машину. Я не могу больше среди этих п*здарванок сидеть',
    'ping': 'Руки убрал, РУКИ УБРАЛ Я СКАЗАЛ! Трогать будешь свою Палину бл*ть.',
    'speak_int': 'Дай договорю.',
    'user_exists': 'Мы с вами уже знакомы',
    'gender_error': 'Ты за меня придурка не держи',
    'gender_not_entered': 'Ты еще не указал пол',
    'gender_male': 'О, это мне нада, будешь мальчиком',
    'gender_female': 'Пездец, и это мне какая-то баба указывать будет?',
    'user_unknown': 'Я тебя вообще не знаю. Чтобы познакомится *поближе* введи *gcreate*'
}

def send_hello(author):
    return (f'Уважаемый {author}. Хочу вас приветствовать и поприветствовать.')

def send_join_error(author):
    return (f'Уважаемый {author}, сначала сам зайди, потом зови. (ты никто и звать тебя никта)')

def send_create_ok(author):
    return (f'Приятно познакомиться, {author}. Хотелось бы узнать твой пол. Введи *ggender male/female*')

def send_gender(gender):
    if (gender == 'male'):
        gender = 'мужчина'
    else:
        gender = 'женщина'
    return (f'Если не ошибаюсь, ты {gender}')

def send_debug(message):
    timestamp = datetime.datetime.now()
    print(f'{timestamp.strftime(r"(%d.%m.%Y) %H:%M:%S")} - {message}')