import datetime

phrases = {
    'on_ready': 'я не сплю',
    'cutie_debug': 'random ganich',
    'join_connect': 'Ну-ка вышли все отсюда. Я щас полицию вызову',
    'join_another': 'Пздец за вами еще бегать блть. Где моё такси, сука?',
    'leave': 'Влад, вызывай мне машину. Я не могу больше среди этих п*здарванок сидеть',
    'ping': 'Руки убрал, РУКИ УБРАЛ Я СКАЗАЛ! Трогать будешь свою Палину бл*ть.'
}

def send_hello(author):
    return (f'Уважаемый {author}. Хочу вас приветствовать и поприветствовать.')

def send_join_error(author):
    return (f'Уважаемый {author}, сначала сам зайди, потом зови. (ты никто и звать тебя никта)')

def send_debug(message):
    timestamp = datetime.datetime.now()
    print(f'{timestamp.strftime(r"(%d.%m.%Y) %H:%M:%S")} - {message}')