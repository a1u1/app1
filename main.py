
import os
import telebot


token = "718226253:AAHHiFDewZ82_dolZVVaT53lbIwwA7RniEk"
bot = telebot.TeleBot(token)
APP_NAME = 'App1928'



print(bot.get_me())

def log(message):
    print("\n ----------")
    from datetime import datetime
    print (datetime.now())
    print ("Сообщение от {0} {1}. (id) = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                             message.from_user.last_name,
                                                             str(message.from_user.id),
                                                             message.text))
    #print(answer)

user_a = "93672279"
user_1 = "93672279"
user_2 = "684010983"


@bot.message_handler(content_types=["text"])
def handle_text(message):



# User 1

    if str(message.from_user.id) == user_1:
        answer = message.text
        bot.send_message(user_2, answer)
        log(message)
        import datetime
        a_answer = "Сообщение от {0} \n --------- \n {1} \n --------- \n {2}".format(message.from_user.first_name,message.text,
                                                     f"{datetime.datetime.now():%Y-%m-%d %H:%M%:%S}")
        bot.send_message(user_a, a_answer)


# User 2

    if str(message.from_user.id) == user_2:
        answer = message.text
        bot.send_message(user_1, answer)
        log(message)
        import datetime
        a_answer = "Сообщение от {0} \n --------- \n {1} \n --------- \n {2}".format(message.from_user.first_name, message.text,
                                                      f"{datetime.datetime.now():%Y-%m-%d %H:%M%:%S}")
        bot.send_message(user_a, a_answer)


bot.polling(none_stop=True, interval=0)
