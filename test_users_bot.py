# подключение библиотек
import speedtest 
from telebot import TeleBot, types

# создадим бота
bot = TeleBot(token='5824792631:AAFNl8Itq8vabO3HTZlR_TAJznjQnMncz18', parse_mode='html') 
st = speedtest.Speedtest()

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
   
    # отправляем ответ на команду '/start'
    bot.send_message(chat_id=message.chat.id, text="Привет,{0.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html')
    bot.send_message(chat_id=message.chat.id, text="Я бот, измеряющий скорость интернета.\nВыбери тип проверки:\n1 - Скорость скачивания\n2 - Скорость загрузки\n3 - Пинг\nТвой выбор:")

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == "1":
         download = st.download()
         bot.send_message(chat_id=message.chat.id, text=(f"{download}"+" bps"))
    elif message.text == "2":
         upload = st.upload()  
         bot.send_message(chat_id=message.chat.id, text=(f"{upload}"+" bps"))
    elif message.text == "3":
        servernames =[]   
        st.get_servers(servernames)   
        pp = st.results.ping
        bot.send_message(chat_id=message.chat.id, text=(f"{pp}" +" ms"))
    else: bot.send_message(chat_id=message.chat.id, text="Пожалуйста,{0.first_name}, введите цифру от 1 до 3!".format(message.from_user, bot.get_me()),parse_mode='html')
       
     
# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()

if __name__ == '__main__':
    main()
