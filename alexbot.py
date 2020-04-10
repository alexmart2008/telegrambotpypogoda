import telebot
import pyowm
owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("1230276509:AAH0s0M7T0e2W6IuFft8VzI1hWjRybaKvhw")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'В каком городе вы хотите узнать температуру?')
@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    if temp < 5 :\
        a = "На улице сейчас очень холодно, одевайся как на северный полюс! "
    elif temp > 5 and temp < 20 :
        a = "На улице сейчас холодновато, одевайся тепло!"
    elif temp > 20 :
        a = "Сейчас жарко, можно гулять в шортах!"
    bot.send_message(message.chat.id,  "В городе " + message.text + " сейчас " + w.get_detailed_status() + "." + "\n" + "Температура сейчас " + str(temp) + "градусов.\n\n" + a)
bot.polling(none_stop=True)