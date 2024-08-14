def send_email(message, recipient, sender="university.help@gmail.com"):
    if not ('@' in recipient and '@' in sender and
            recipient.endswith(('.ru', '.com', '.net')) and
            sender.endswith(('.ru', '.com', '.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient} с текстом {message}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'sk@bk.ru')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
