from telebot import TeleBot
from envparse import Env

'''LINK = t.me/Home_Work_15_Bot'''
env = Env()
TOKEN = env.str('TOKEN')

bot = TeleBot(token=TOKEN)


def subscriber(profile_id):
    print(f'Подписал профиль с id: {profile_id}')


@bot.message_handler(commands=['hello'])
def simple_handler(message):
    profile_id = message.text.split()[1]
    subscriber(profile_id)


bot.polling()
