import string
import random
from datetime import datetime


def generate_password(elems):
    range = int(elems[0]) if elems[0] else 18
    chars_lower = True if elems[1] else False
    chars_upper = True if elems[2] else False
    nums = True if elems[3] else False
    symbbol = True if elems[4] else False
    elements = ""
    default = string.ascii_letters
    if chars_lower:
        elements += string.ascii_lowercase
    if chars_upper:
        elements += string.ascii_uppercase
    if nums:
        elements += string.digits
    if symbbol:
        elements += string.punctuation
    if elements:
        return ''.join(random.choices(elements, k=range))
    else:
        return ''.join(random.choices(default, k=range))


def get_text(check_text):
    text = 'Прекрасный день'
    if check_text.rstrip() == 'Sunny':
        text = 'Солнечно'
    if check_text.rstrip() == 'Cloudy':
        text = 'Облачно'
    if check_text.rstrip() == 'Overcast':
        text = 'Пасмурная погода'
    if check_text.rstrip() == 'Mist':
        text = 'Туман'
    if check_text.rstrip() == 'Blizzard':
        text = 'Метель'
    if check_text.rstrip() == 'Patchy rain possible':
        text = 'Кратковременный дождь'
    if check_text.rstrip() == 'Patchy snow possible':
        text = 'Кратковременный снег'
    if check_text.rstrip() == 'Fog':
        text = 'Туман'
    if check_text.rstrip() == 'Heavy snow':
        text = 'Сильный снегопад'
    if check_text.rstrip() == 'Light snow':
        text = 'Легкий снег'
    if check_text.rstrip() == 'Heavy rain':
        text = 'Ливень'
    if check_text.rstrip() == 'Light drizzle':
        text = 'Небольшой дождь'
    if check_text.rstrip() == 'Partly Cloudy':
        text = 'Переменная облачность'
    if check_text.rstrip() == 'Patchy sleet possible':
        text = 'Возможен мокрый снег'
    if check_text.rstrip() == 'Light sleet showers':
        text = 'Ливень с мокрым снегом'
    if check_text.rstrip() == 'Light rain shower':
        text = 'Небольшой дождь'
    if check_text.rstrip() == 'Moderate or heavy rain shower':
        text = 'Умеренный ливень'
    if check_text.rstrip() == "Patchy rain nearby":
        text = "Неподалеку дождь"

    return text


days_translation = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
    'Sunday': 'Воскресенье'
}


def get_week(year, month, day):
    date_obj = datetime(year, month, day)
    day_of_week = date_obj.strftime('%A')
    week = days_translation[day_of_week]
    return week


def get_parametrs(response):
    time = response['location']['localtime']
    hours = time[11:16]
    time_obj = datetime.strptime(time, '%Y-%m-%d %H:%M')
    day_of_week = time_obj.strftime('%A')
    day_of_week_ru = days_translation[day_of_week]
    name = response['location']['name']
    region = response['location']['region']
    country = response['location']['country']
    temp = response['current']['temp_c']
    wind = response['current']['wind_kph']
    humidity = response['current']['humidity']
    cloud = response['current']['cloud']
    icon = response['current']['condition']['icon']
    check_text = response['current']['condition']['text']
    is_day = response['current']['is_day']
    uv = response['current']['uv']
    text = get_text(check_text)
    context = {
        'time': hours,
        'name': name,
        'region': region,
        'country': country,
        'temp': temp,
        'wind': wind,
        'humidity': humidity,
        'icon': icon,
        'cloud': cloud,
        'is_day': is_day,
        'text': text,
        'uv': uv,
        'week': day_of_week_ru,
        'status': True
    }
    return context
